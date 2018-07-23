from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class User(models.Model):
    account         =   models.ForeignKey(user,on_delete=models.CASCADE)
    profile_picture =   models.ImageField(upload_to = 'static/media')
    last_name       =   models.CharField(max_length=100)
    first_name      =   models.CharField(max_length=100)
    middle_name     =   models.CharField(max_length=200)
    sex             =   models.CharField(max_length=6, choices=GENDER, blank=True, default=True)
    date_of_birth   =   models.DateField()
    age             =   models.CharField(max_length=20)
    student         =   models.BooleanField(default=False)
    teacher         =   models.BooleanField(default=False)
    office          =   models.BooleanField(default=False)
    Location        =   models.CharField(max_length=100)
    Bio             =   models.TextField(blank=True, default=True)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return '{}'.format(self.last_name, self.first_name)

class org(models.Model):
    member          = models.ManyToManyField(User)
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
