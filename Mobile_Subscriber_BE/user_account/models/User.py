from django.conf import settings
from django.db import models
# from account.models.BaseModel import BaseModel
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

from user_account.models.BaseModel import BaseModel


class UserManager(BaseUserManager):
    """
    Overiding the default UserManager as it is required
    when creating a custom User. 
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a `User` with a email and password."""

        if not email:
            raise ValueError(_('Users must have an email.'))

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, password):
        """
        Creates a user with staff priveledges
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a user with superuser priveledges
        """
        if not password:
            raise TypeError(_('Superusers must have a password.'))

        user = self.create_user(
            email, password=password,
            **extra_fields)
        user.is_superuser = True
        user.staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):

    email = models.EmailField(
        'Email',
        # db_index=True,
        max_length=100,
        unique=True
    )

    firstname = models.CharField(
        'First name',
        null=True,
        max_length=255,
        default=None
    )

    othernames = models.CharField(
        'Other names',
        null=True,
        max_length=100,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    staff = models.BooleanField(
        default=False
    )

    admin = models.BooleanField(
        default=False
    )

    verified = models.BooleanField(
        default=True
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        # app_label = 'user_account'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_verified(self):
        return self.verified

    def __str__(self):
        """
        String representaion for a 'User' object
        """
        return f"User: {self.email} "

    def get_full_name(self):
        return f"{self.firstname} {self.othernames} {self.email}"

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def token(self):
        token = jwt.encode(
            {'email': self.email,
             'exp': datetime.now()+timedelta(hours=2),
             },
            settings.SECRET_KEY,
            algorithm="HS256"
        )
        return token
