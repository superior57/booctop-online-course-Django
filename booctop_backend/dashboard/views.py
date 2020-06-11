from django.shortcuts import render

def home_page_view(request):
	return render(request, 'dashboard/index.html')

def become_teacher_view(request):
	return render(request, 'dashboard/become.html')

def user_signup_view(request):
	return render(request, 'dashboard/signup.html')

def signle_course_view(request):
	return render(request, 'dashboard/single_course.html')
