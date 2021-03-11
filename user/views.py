from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_list(request):
	return render(request,'user/user.html')
