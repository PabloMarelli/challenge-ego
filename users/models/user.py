from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone

class UserManager(BaseUserManager):
    """User management"""
    
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves new user.
        """
        
        if not email:
            raise ValueError("Users must have an email.")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create superuser
        """
        
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model
    
    Email as login field, email and password are required, other are optional.
    
    """
    
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.CharField(max_length=255)
    date_joined = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def get_absolute_url(self):
        return "users/%i" % (self.pk)
    
    