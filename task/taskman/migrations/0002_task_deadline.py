# Generated by Django 4.1.2 on 2022-10-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
