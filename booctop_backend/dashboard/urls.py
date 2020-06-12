from django.urls import path
from dashboard import views

urlpatterns = [
	path('', views.home_page_view, name='index'),
	path('signup/', views.user_signup_view, name='user_signup'),
	path('account-activation/<uuid:activation_code>/', views.account_activation_view, name='account_activation'),
	path('login/', views.user_login_view, name='user_login'),
	path('logout/', views.user_logout_view, name='user_logout'),
	path('become-teacher/', views.become_teacher_view, name='become_teacher'),
	path('course/', views.single_course_view, name='single_course'),
	path('category/', views.single_category_view, name='single_category'),
	path('wishlist/', views.wishlist_view, name='wishlist'),
	path('cart/', views.cart_view, name='cart'),
	path('checkout/', views.checkout_view, name='checkout'),
	path('about/', views.about_page_view, name='about'),
	path('faq/', views.faq_page_view, name='faq'),
	path('support/', views.support_page_view, name='support'),
	path('terms-condition/', views.terms_view, name='terms'),
	path('page-not-found/', views.page_not_found_view, name='page_not_found'),
	#Ajax
	path('email-checking/', views.check_email_view, name='check_email'),
]