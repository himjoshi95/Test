# Generated by Django 4.1.2 on 2022-10-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskman', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='email_address',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
