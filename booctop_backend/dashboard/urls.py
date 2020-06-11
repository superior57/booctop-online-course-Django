from django.urls import path
from .views import home_page_view, become_teacher_view, user_signup_view, user_login_view, signle_course_view, check_email_view

urlpatterns = [
	path('', home_page_view, name='index'),
	path('become-teacher/', become_teacher_view, name='become_teacher'),
	path('signup/', user_signup_view, name='user_signup'),
	path('login/', user_login_view, name='user_login'),
	path('course/', signle_course_view, name='signle_course'),
	#Ajax
	path('email-checking/', check_email_view, name='check_email'),
]