from django.urls import path
from teacher.views import store_course, store_course_2, store_course_3, getCourseDetailsById

urlpatterns = [
    path('store-course', store_course, name="store course"),
    path('store-course-2', store_course_2, name="store course2"),
    path('store-course-3', store_course_3, name="store course3"),    
    path('get-coursedetails', getCourseDetailsById, name="get course details"),
]