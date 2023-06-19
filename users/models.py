import datetime
import random

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

import choices


class CredentialManager(BaseUserManager):
    def create_superuser(self, password=None, email=None):
        user = self.create_user(password=password, email=email)
        user.is_django_admin = True
        user.is_active = True
        user.save()
        return user

    def create_user(self, phone=None, password=None, email=None, employee_id=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def add_user_with_all_data(
            self,
            id=None,
            is_approved=False,
            is_active=False,
            created_at=datetime.datetime.now(),
            modified_at=datetime.datetime.now(),
            email=None,
            phone=None,
            password=None,
            is_admin=False,
            is_django_admin=False,
            employee_id=None,
            last_login=datetime.datetime.now()
    ):
        credential = self.model(
            is_approved=is_approved,
            is_active=is_active,
            created_at=created_at,
            modified_at=modified_at,
            email=email,
            phone=phone,
            password=password,
            is_admin=is_admin,
            is_django_admin=is_django_admin,
            employee_id=employee_id,
            last_login=last_login
        )
        if id:
            credential.id = id
        credential.save()
        return credential

# for every user
class CredentialsData(AbstractBaseUser):
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(verbose_name='email', max_length=200,
                              unique=True, default=None, null=True, blank=True)
    # phone = models.BigIntegerField(unique=True, verbose_name='Phone number', default=None, null=True, blank=True)
    otp = models.CharField(null=True, blank=True, default=None, max_length=6)
    is_admin = models.BooleanField(default=False)
    is_django_admin = models.BooleanField(default=False)
    # employee_id = models.CharField(unique=True, max_length=9, default=None, null=True, blank=True, verbose_name='Employee ID')

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['email', 'phone']

    objects = CredentialManager()

    def __str__(self):
        return '%s' % (self.email)

    def is_staff(self):
        return self.is_django_admin

    @staticmethod
    def has_module_perms(obj=None):
        return True

    @staticmethod
    def has_perm(obj=None):
        return True

    class Meta:
        verbose_name = "Credential"
        verbose_name_plural = "Credentials"

    def save(self, *args, **kwargs):
        if self.email is not None:
            self.email = self.email.lower().strip()
            if self.email == "":
                raise ValidationError(
                    _("%(self.email) is not an valid email"),
                    params={"email": self.email},
                )
        super(CredentialsData, self).save(*args, **kwargs)




def random_number():
    id_no = random.randint(1000, 2147400000)
    return id_no


class UsersData(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='first name')
    last_name = models.CharField(
        max_length=100, verbose_name='last name', blank=True, null=True, default=None)
    date_of_birth = models.DateField(
        verbose_name='date of birth', blank=True, null=True, default=None)
    modules_access = models.JSONField(blank=True, null=True)
    phone = models.CharField(max_length=10, unique=True, blank=True, null=True, default=None)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    credentials = models.ForeignKey(
        CredentialsData, on_delete=models.PROTECT)
    role = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(
        max_length=30, choices=choices.users_status_choices, null=True, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not UsersData.objects.filter(id=self.id).exists():
            self.id = random_number()
            while UsersData.objects.filter(id=self.id).exists():
                self.id = random_number()
        super(UsersData, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


# class PhoneNumbers(models.Model):
#     phone_number = models.CharField(null=False, max_length=10, blank=False)
#     user = models.ForeignKey(
#         UsersData, related_name="phone_numbers", on_delete=models.PROTECT)
#     created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
#     USERNAME_FIELD = "user"

#     def save(self, *args, **kwargs):
#         if not PhoneNumbers.objects.filter(id=self.id).exists():
#             self.id = random_number()
#             while PhoneNumbers.objects.filter(id=self.id).exists():
#                 self.id = random_number()
#         super(PhoneNumbers, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name_plural = "Phone numbers"


# class Emails(models.Model):
#     email = models.EmailField(null=False, blank=False, unique=False)
#     user = models.ForeignKey(
#         UsersData, related_name="emails", on_delete=models.PROTECT)
#     created_at = models.DateTimeField(auto_now=True, null=False, blank=False)

#     def save(self, *args, **kwargs):
#         if not Emails.objects.filter(id=self.id).exists():
#             self.id = random_number()
#             while Emails.objects.filter(id=self.id).exists():
#                 self.id = random_number()
#         super(Emails, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name_plural = "Emails"

#     def __str__(self):
#         return self.email
