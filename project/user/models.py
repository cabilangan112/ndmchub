from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
     BaseUserManager, AbstractBaseUser
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class org(models.Model):
 
    org_name        = models.CharField(max_length=200)
    description     = models.TextField(null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now_add=True)
    private         = models.BooleanField(default=False)
    public          = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return '{}'.format(self.org_name)


class info(models.Model):
    account         =   models.ForeignKey('Account',on_delete=models.CASCADE)
    profile_picture =   models.ImageField(upload_to = 'static/media')
    first_name      =   models.CharField(max_length=40, blank=True)
    last_name       =   models.CharField(max_length=40, blank=True)      
    tagline         =   models.CharField(max_length=140, blank=True)
    sex             =   models.CharField(max_length=6, choices=GENDER, blank=True, default=True)
    age             =   models.CharField(max_length=20)
    Location        =   models.CharField(max_length=100)      
    Bio             =   models.TextField(blank=True, default=True)
    student         =   models.BooleanField(default=False)
    teacher         =   models.BooleanField(default=False)
    office          =   models.BooleanField(default=False)

class AccountManager(BaseUserManager):
    def create_user(self, email,date_of_birth, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')
        account = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(self, email,  date_of_birth, password, **kwargs):
        account = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        account.is_admin = True
        account.save(using=self._db)
        return account

class Account(AbstractBaseUser):
    email           =   models.EmailField(unique=True)
    username        =   models.CharField(max_length=40, unique=True)
    sex             =   models.CharField(max_length=6, choices=GENDER, blank=True, default=True)
    date_of_birth   =   models.DateField()
    is_admin        =   models.BooleanField(default=False)
    created_at      =   models.DateTimeField(auto_now_add=True)
    updated_at      =   models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']


    def __str__(self):
        return '{}'.format(self.email)
 


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin