from django.urls import path
from student.views import account, courses, options_settings, security, payments, privacy, quizes, quizes2, certificates, PurchaseHistory, messages, notifications


urlpatterns = [
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
]