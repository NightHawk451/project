from django.shortcuts import render

# Create your views here.

def home(request):
	if request.user.is_quthenticated():
		print(request.user.profile.first_nm)
	context = {}
	return render(request,"home.html",context)