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
from django.conf.urls import include, url
from django.conf.urls.static import static
from home.views import saveimg, getsubcategory, changepassword, update_user, home_view, signup, about, faqs, help, terms, become, single_category, single_course, register_user, activation, ajaxlogin, logout_, check_email
from student.views import account, courses, options_settings, security, payments, privacy, quizes, quizes2, certificates, PurchaseHistory, messages, notifications
from teacher.views import teacher_account, teacher_privacy, teacher_notifications, teacher_courses, teacher_security, teacher_payments, teacher_messages, teacher_faqs, teacher_help, course_engagement, student_performance, dashboard, dashboard1, guideline, help2, newcourse2, newcourse3, newcourse4, newcourse5, newcourse, nocourseengagement, nocourse
from video.views import playground, video_quiz, video_quiz2, video_quiz3


urlpatterns = [
    path('admin/', admin.site.urls),
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
    
    
    
    
    # Student Urls
    path('account', account, name='student account'),
    path('courses', courses, name='student courses'),
    path('security', security, name='student security'),
    path('payments', payments, name='student payments'),
    path('privacy', privacy, name='student privacy'),
    path('quizes', quizes, name='student quizes'),
    path('quizes2', quizes2, name='student quizes2'),
    path('certificates', certificates, name='student certificates'),
    path('PurchaseHistory', PurchaseHistory, name='student PurchaseHistory'),
    path('messages', messages, name='student messages'),
    path('notifications', notifications, name='student notifications'),

    #Teacher Urls  
    path('teacher/account', teacher_account, name='teacher dashboard'),
    path('teacher/security', teacher_security, name='teacher security'),
    path('teacher/courses', teacher_courses, name='teacher courses'),
    path('teacher/payments', teacher_payments, name='teacher payments'),
    path('teacher/new-course-2', teacher_privacy, name='teacher privacy'),
    path('teacher/notifications', teacher_notifications, name='teacher notifications'),
    path('course-engagement', course_engagement, name='teacher course-engagement'),
    path('student-performance', student_performance, name='teacher student-performance'),
    path('teacher/messages', teacher_messages, name='teacher messages'),
    path('teacher/faqs', teacher_faqs, name='teacher faqs'),
    path('teacher/help', teacher_help, name='teacher help'),
    path('teacher/privacy', teacher_privacy, name='teacher privacy'),
    
    path('dashboard-1', dashboard1, name='teacher dashboard-1'),
    path('teacher/dashboard', dashboard, name='teacher dashboard'),
    path('guideline', guideline, name='teacher guideline'),
    path('help2', dashboard, name='teacher help2'),
    path('new-course-2', newcourse2, name='teacher new-course-2'),
    path('new-course-3', newcourse3, name='teacher new-course-3'),
    path('new-course-4', newcourse4, name='teacher new-course-4'),
    path('new-course-5', newcourse5, name='teacher new-course-5'),
    path('new-course', newcourse, name='teacher new-course'),
    path('no-course-engagement', nocourseengagement, name='teacher no-course-engagement'),
    path('no-course', nocourse, name='teacher no-course'),

    # includes
    url(r'', include('teacher.urls')),

    #Video url
    path('video/playground', playground, name='video playground'),
    path('video/quiz', video_quiz, name='video quiz'),
    path('video/quiz2', video_quiz2, name='teacher quiz2'),
    path('video/quiz3', video_quiz3, name='teacher quiz3'),




    

]
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
