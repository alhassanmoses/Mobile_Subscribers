from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from account.models import BaseModel


class UserManager(BaseUserManager):
    """
    Overiding the default UserManager as it is required
    when creating a custom User. 
    """

    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a `User` with a username and password."""

        if not username:
            raise TypeError('Users must have a valid username.')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Creates a user with superuser priveledges
        """
        if not password:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            username, email, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):

    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        """
        String representaion for a 'User' object
        """
        return f"User: {self.username} "

    def get_short_name(self):

        return self.first_name
