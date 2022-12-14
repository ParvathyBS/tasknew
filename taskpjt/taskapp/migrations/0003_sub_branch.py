# Generated by Django 4.1.1 on 2022-12-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_remove_branch_sub_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'subbranch',
                'verbose_name_plural': 'subbranches',
                'ordering': ('name',),
            },
        ),
    ]
