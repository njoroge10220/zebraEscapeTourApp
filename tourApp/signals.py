
from django.contrib.auth.signals import user_logged_in
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    subject = 'Welcome Back!'
    message = f'Hi {user.username},\n\nThank you for logging back into our website.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    send_mail(subject, message, email_from, recipient_list)