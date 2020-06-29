from django.urls import path
from django.contrib import admin
from home.views import saveimg, getsubcategory, changepassword, update_user, home_view, signup, about, faqs, help, terms, become, single_category, single_course, register_user, activation, ajaxlogin, logout_, check_email
from student.views import options_settings


urlpatterns = [
    
    path('', home_view, name='home'),
    path('signup', signup, name='signup'),
    path('register-user', register_user, name='register'),
    path('update-user', update_user, name='update'),
    path('about', about, name='about'),
    path('faqs', faqs, name='faqs'),
    path('help', help, name='help'),
    path('terms', terms, name='terms'),
    path('become', become, name='become'),
    path('single_category', single_category, name='single_category'),
    path('single_course', single_course, name='single_course'),
    path('activation', activation, name='activation'),
    path('options-settings', options_settings, name='options settings'),
    path('check-email', check_email, name='check email'),
    path('login', ajaxlogin, name='login'),
    path('logout', logout_, name='logout'),
    path('saveimg', saveimg, name='saveimg'),
    path('getsubcategory', getsubcategory, name='getsubcategory'),
    path('changepassword', changepassword, name='changepassword'),

    # Arabic
    path('ar', home_view, name='home'),
    path('ar/signup', signup, name='signup'),

]