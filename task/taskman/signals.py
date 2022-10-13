from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Task
from django.utils.text import slugify

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print('user {} logged in through page {}'.format(user.username,request.META.get('HTTP_REFERER')))

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    print('user {} failed to login through page {}'.format(request.META.get('HTTP_REFERER')))

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print('user {} logged out through page {}'.format(user.username,request.META.get('HTTP_REFERER')))

@receiver(post_save, sender=Task)
def create_task(sender, instance, created, **kwargs):

    if created:
        title = instance.title
        print(f'Task Created {title}')

@receiver(post_save, sender=Task)
def update_task(sender, instance, created, **kwargs):

    if created == False:
        title = instance.title
        print(f'Task Updated {title}')

@receiver(post_delete,sender =Task)
def delete_task(sender, instance,*args,**kwargs):
    print(f'Task Deleted {instance.title}')