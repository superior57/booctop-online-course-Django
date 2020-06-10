from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html', {})


def signup(request):
    return render(request, 'signup.html', {})    

def about(request):
    return render(request, 'about.html', {})  

def faqs(request):
    return render(request, 'faqs.html', {})  
    

def help(request):
    return render(request, 'support.html', {})  

def terms(request):
    return render(request, 'terms.html', {})

def become(request):
    return render(request, 'become.html', {})



def single_category(request):
    return render(request, 'single_category.html', {})

