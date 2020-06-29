from django.urls import path
from video.views import playground, video_quiz, video_quiz2, video_quiz3


urlpatterns = [
    path('video/playground', playground, name='video playground'),
    path('video/quiz', video_quiz, name='video quiz'),
    path('video/quiz2', video_quiz2, name='teacher quiz2'),
    path('video/quiz3', video_quiz3, name='teacher quiz3'),
]