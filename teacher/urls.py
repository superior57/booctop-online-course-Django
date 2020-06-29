from django.urls import path
from teacher.views import store_course, store_course_2, store_course_3, getCourseDetailsById, teacher_account, teacher_privacy, teacher_notifications, teacher_courses, teacher_security, teacher_payments, teacher_messages, teacher_faqs, teacher_help, course_engagement, student_performance, dashboard, dashboard1, guideline, help2, newcourse2, newcourse3, newcourse4, newcourse5, newcourse, nocourseengagement, nocourse


urlpatterns = [
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


    # posts

    path('store-course', store_course, name="store course"),
    path('store-course-2', store_course_2, name="store course2"),
    path('store-course-3', store_course_3, name="store course3"),    
    path('get-coursedetails', getCourseDetailsById, name="get course details"),
]