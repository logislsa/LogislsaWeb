# Generated by Django 3.2 on 2021-04-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('companyID', models.CharField(default=None, max_length=30, unique=True, verbose_name='Company ID')),
                ('companyName', models.CharField(default=None, max_length=30, verbose_name='Company')),
                ('companyEmail', models.EmailField(default=None, max_length=30, verbose_name='Company Email')),
                ('vesselList', models.TextField(max_length=1200, verbose_name='Vessel List')),
                ('CPNpassword', models.CharField(default=None, max_length=30, verbose_name='Password')),
            ],
            options={
                'db_table': 'shipping_company_table',
            },
        ),
    ]