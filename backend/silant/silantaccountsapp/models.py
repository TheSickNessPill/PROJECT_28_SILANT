from typing import Any
import datetime

from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import (
    UserManager, User, AbstractBaseUser,PermissionsMixin
)


class SilantUserManager(UserManager):
    def _creater_user(self, username: str, password: str, **extra_fields: Any) -> User:
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username: str, password: str, **extra_fields: Any):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._creater_user(username, password, **extra_fields)

    def create_superuser(self, username: str, password: str, **extra_fields: Any):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._creater_user(username, password, **extra_fields)


class SilantUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=60, blank=False, null=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    session_duration = models.IntegerField(blank=True, null=True, default=24)
    company_name = models.TextField(blank=True, null=True)

    objects = SilantUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.username}"

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def login(self):
        now = datetime.datetime.now(datetime.UTC)
        self.last_login = now
        token, is_created = Token.objects.get_or_create(user=self)
        self.save()

        return token.key

    def logout(self):
        Token.objects.filter(user=self).delete()
        self.save()

        return True

    def is_session_expired(self):
        if not self.last_login:
            return True

        now = datetime.datetime.now(datetime.UTC)

        return (now - self.last_login) > datetime.timedelta(hours=self.session_duration)

    def get_expired_time(self):
        expired_time = self.last_login + datetime.timedelta(hours=24)
        print("expired_time", expired_time)
        return expired_time.isoformat()

class SilantRolesAccess(models.Model):
    role_name = models.CharField(max_length=64, blank=False, null=False)
    role_access = models.JSONField(blank=False, null=False)

    def __str__(self) -> str:
        return self.role_name


class SilantClients(models.Model):
    user = models.OneToOneField(SilantUser, on_delete=models.CASCADE)
    access = models.ForeignKey(SilantRolesAccess, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} {self.user.company_name}"

class SilantServiveCompanies(models.Model):
    user = models.OneToOneField(SilantUser, on_delete=models.CASCADE)
    access = models.ForeignKey(SilantRolesAccess, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} {self.user.company_name}"

class SilantManagers(models.Model):
    user = models.OneToOneField(SilantUser, on_delete=models.CASCADE)
    access = models.ForeignKey(SilantRolesAccess, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}"