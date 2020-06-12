from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile, TermsAndConditions
from django.utils.crypto import get_random_string
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import uuid
import datetime
from django.utils import timezone
from .emails import send_account_activation_mail
from django.conf import settings

def home_page_view(request):
	return render(request, 'dashboard/index.html')

def user_signup_view(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		phone_number = request.POST.get('phone_number')
		user_type = request.POST.get('user_type')

		user = User.objects.create(first_name=first_name, last_name=last_name, email=email, is_active=False)
		user.username = get_random_string(length=8)
		user.set_password(password)
		user.save()

		activation_code = uuid.uuid4()
		user_profile = UserProfile.objects.create(user=user, phone_number=phone_number, user_type=user_type, activation_code=activation_code)

		send_account_activation_mail(user, activation_code)

		return JsonResponse({'success':True})
	
	return render(request, 'dashboard/signup.html')

def account_activation_view(request, activation_code):
	valid_time = timezone.now() - datetime.timedelta(days=1)
	user = UserProfile.objects.get(activation_code=activation_code).user
	if valid_time < user.date_joined:
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('index')
	return redirect('page_not_found')
	
def user_login_view(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		
		user_objects = User.objects.filter(email=email, is_active=True)
		if not user_objects.exists():
			return JsonResponse({'email_error':True})

		if not user_objects[0].check_password(password):
			return JsonResponse({'password_error':True})
		
		username = user_objects[0].username
		user = authenticate(username=username, password=password)
		login(request, user)
		return JsonResponse({'success':True})

	return render(request, 'dashboard/index.html')

@login_required
def user_logout_view(request):
	logout(request)
	return JsonResponse({'success':True})

#Ajax
def check_email_view(request):
	email = request.GET.get('email')
	valid = True
	user = User.objects.filter(email=email)
	if user.exists():
		valid = False
	return JsonResponse({'valid':valid})

def become_teacher_view(request):
	return render(request, 'dashboard/become.html')

def single_course_view(request):
	return render(request, 'dashboard/single_course.html')

def single_category_view(request):
	return render(request, 'dashboard/single_category.html')

def cart_view(request):
	if not request.user.is_authenticated:
		return redirect('index')
	return render(request, 'dashboard/cart.html')

def wishlist_view(request):
	return render(request, 'dashboard/wishlist.html')

def checkout_view(request):
	return render(request, 'dashboard/checkout.html')

def about_page_view(request):
	return render(request, 'dashboard/about.html')

def faq_page_view(request):
	return render(request, 'dashboard/faq.html')

def support_page_view(request):
	return render(request, 'dashboard/support.html')

def terms_view(request):
	terms_objects = TermsAndConditions.objects.filter(version=settings.VERSION)
	context = {
		'terms_objects' : terms_objects
	}
	return render(request, 'dashboard/terms.html', context)

def page_not_found_view(request):
	return render(request, 'dashboard/404.html')