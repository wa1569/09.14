# Generated by Django 3.2 on 2021-09-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(default='이메일을 입력해 주세요.', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='old',
            field=models.CharField(default='나이를 입력해 주세요.', max_length=2),
        ),
    ]
