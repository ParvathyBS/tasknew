# Generated by Django 4.1.1 on 2022-12-14 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='sub_branch',
        ),
    ]