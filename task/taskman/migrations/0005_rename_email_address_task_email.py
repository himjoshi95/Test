# Generated by Django 4.1.2 on 2022-10-11 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskman', '0004_task_email_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='email_address',
            new_name='email',
        ),
    ]