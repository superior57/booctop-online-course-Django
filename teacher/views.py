from django.shortcuts import render

def teacher_account(request):
    return render(request, 'teacher/account.html', {})

def teacher_security(request):
    return render(request, 'teacher/security.html', {})

def teacher_notifications(request):
    return render(request, 'teacher/notifications.html', {})
    
def teacher_payments(request):
    return render(request, 'teacher/payments.html', {})

def teacher_privacy(request):
    return render(request, 'teacher/privacy.html', {})

def dashboard(request):
    return render(request, 'teacher/dashboard.html', {}) 

def teacher_courses(request):
    return render(request, 'teacher/courses.html', {}) 

def teacher_faqs(request):
    return render(request, 'teacher/faqs.html', {}) 

def course_engagement(request):
    return render(request, 'teacher/course-engagement.html', {})  

def student_performance(request):
    return render(request, 'teacher/student-performance.html', {})  
    
def teacher_messages(request):
    return render(request, 'teacher/messages.html', {})  
      

def dashboard1(request):
    return render(request, 'teacher/dashboard_1.html', {})    

def guideline(request):
    return render(request, 'teacher/guidline.html', {})    
    
def teacher_help(request):
    return render(request, 'teacher/help.html', {})    

def help2(request):
    return render(request, 'teacher/help2.html', {})    

def newcourse2(request):
    return render(request, 'teacher/new-course-2.html', {})    

def newcourse3(request):
    return render(request, 'teacher/new-course-3.html', {})    

def newcourse4(request):
    return render(request, 'teacher/new-course-4.html', {})    

def newcourse5(request):
    return render(request, 'teacher/new-course-5.html', {})    

def newcourse(request):
    return render(request, 'teacher/new-course.html', {})    

def nocourseengagement(request):
    return render(request, 'teacher/no-course-engagement.html', {})    

def nocourse(request):
    return render(request, 'teacher/no-course.html', {})    

