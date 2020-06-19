from django.shortcuts import render

def account(request):
    print("requesting - ", request)
    return render(request, 'student/account.html', {})
    
def courses(request):
    return render(request, 'student/courses.html', {})

def options_settings(request):
    return render(request, 'student/courses.html', {})

def security(request):
    return render(request, 'student/security.html', {})

def payments(request):
    return render(request, 'student/payments.html', {})

def privacy(request):
    return render(request, 'student/privacy.html', {})    

def quizes(request):
    return render(request, 'student/quizes.html', {})      

def certificates(request):
    return render(request, 'student/certificates.html', {})     

def PurchaseHistory(request):
    return render(request, 'student/PurchaseHistory.html', {})    

def messages(request):
    return render(request, 'student/messages.html', {})    

def notifications(request):
    return render(request, 'student/notifications.html', {}) 

def quizes2(request):
    return render(request, 'student/quizes-2.html', {}) 