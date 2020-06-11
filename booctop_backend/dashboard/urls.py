from django.urls import path
from .views import home_page_view, become_teacher_view, user_signup_view, signle_course_view

urlpatterns = [
	path('', home_page_view, name='index'),
	path('become-teacher/', become_teacher_view, name='become_teacher'),
	path('signup/', user_signup_view, name='user_signup'),
	path('course/', signle_course_view, name='signle_course'),
]