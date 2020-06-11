"""booctop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home_view, signup, about, faqs, help, terms, become, single_category, single_course, register_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup', signup, name='signup'),
    path('register-user', register_user, name='signup'),
    path('about', about, name='about'),
    path('faqs', faqs, name='faqs'),
    path('help', help, name='help'),
    path('terms', terms, name='terms'),
    path('become', become, name='become'),
    path('single_category', single_category, name='single_category'),
    path('single_course', single_course, name='single_course'),

]
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
