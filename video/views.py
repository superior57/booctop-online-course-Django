from django.shortcuts import render

def playground(request):
    return render(request, 'video/playground.html', {})

def video_quiz(request):
    return render(request, 'video/quiz.html', {})

def video_quiz2(request):
    return render(request, 'video/quiz2.html', {})

def video_quiz3(request):
    return render(request, 'video/quiz3.html', {})
