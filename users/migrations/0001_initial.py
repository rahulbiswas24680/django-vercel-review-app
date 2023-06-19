# Generated by Django 4.2.1 on 2023-05-26 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=200, null=True, unique=True, verbose_name='email')),
                ('otp', models.CharField(blank=True, default=None, max_length=6, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_django_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Credential',
                'verbose_name_plural': 'Credentials',
            },
        ),
        migrations.CreateModel(
            name='UsersData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='last name')),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True, verbose_name='date of birth')),
                ('modules_access', models.JSONField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=10, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('cancelled', 'Cancelled')], max_length=30, null=True)),
                ('credentials', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.credentialsdata')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='phone_numbers', to='users.usersdata')),
            ],
            options={
                'verbose_name_plural': 'Phone numbers',
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='emails', to='users.usersdata')),
            ],
            options={
                'verbose_name_plural': 'Emails',
            },
        ),
    ]
