from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.crypto import get_random_string
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate

def home_page_view(request):
	return render(request, 'dashboard/index.html')

def become_teacher_view(request):
	return render(request, 'dashboard/become.html')

def signle_course_view(request):
	return render(request, 'dashboard/single_course.html')

def user_signup_view(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		phone_number = request.POST.get('phone_number')
		user_type = request.POST.get('user_type')

		user = User.objects.create(first_name=first_name, last_name=last_name, email=email)
		user.username = get_random_string(length=8)
		user.set_password(password)
		user.save()

		user_profile = UserProfile.objects.create(user=user, phone_number=phone_number, user_type=user_type)

		return JsonResponse({'success':True})
	
	return render(request, 'dashboard/signup.html')

def user_login_view(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		
		user_objects = User.objects.filter(email=email)
		if not user_objects.exists():
			return JsonResponse({'email_error':True})
		
		username = user_objects[0].username
		user = authenticate(username=username, password=password)
		if not user:
			return JsonResponse({'password_error':True})

		login(request, user)
		return redirect('index')

#Ajax
def check_email_view(request):
	email = request.GET.get('email')
	valid = True
	user = User.objects.filter(email=email)
	if user.exists():
		valid = False
	return JsonResponse({'valid':valid})
