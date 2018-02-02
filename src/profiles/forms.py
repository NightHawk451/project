from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import RegexValidator
from django.db.models import Q

from .models import USERNAME_REGEX

User = get_user_model() # will get customer user model or default user model

#from .models import MyUser

class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get("query")
        password = self.cleaned_data.get("password")
        # user_qs1 = User.objects.filter(username__iexact=query)
        # user_qs2 = User.objects.filter(email__iexact=query)
        # user_qs_final = (user_qs1 | user_qs2).distinct()
        user_qs_final = User.objects.filter(
            Q(user__iexact=query)|
            Q(email__iexact=query)
            ).distinct()
        if not user_qs_final.exists() and user_qs_final.count() != 1:
            raise forms.ValidationError("Invalid credentials")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password): # checks that password is correct
            raise forms.ValidationError("Invalid credentials")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)


    # def clean_username(self): #checks that user exists
    #     username = self.cleaned_data.get('username')
    #     user_qs = User.objects.filter(username=username).exists()
    #     user_exists = user_qs.exists()
    #     if not user_exists and user_qs.count() != 1:
    #         raise forms.ValidationError("Invalid credentials")
    #     return username



#this form will be on the website for users
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User # instead of MyUser
        fields = ('username', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# this form will stay in the admin
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]