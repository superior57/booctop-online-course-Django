from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_account_activation_mail(user, activation_code):
	activation_link = settings.PROJECT_URL + 'account-activation/' + str(activation_code)
	subject = 'Activate Account'
	message = "Hello " + user.first_name + ' ' + user.last_name + '\n\nCongratulations, you successfully created your account. Please follow below link to activate your account \n\n' + 'link - ' + activation_link + '\n\nThis link valid only for 24 hour \n\n\nThank you\nBooctop'
	from_email = settings.EMAILS[0]
	to = [user.email]
	email = EmailMultiAlternatives(subject, message, from_email, to)
	email.send()