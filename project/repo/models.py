from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL


class repo(models.Model):
    owner           = models.ForeignKey(user,on_delete=models.CASCADE)
    repository_name = models.CharField(max_length=150)
    description     = models.TextField(null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now_add=True)
    private         = models.BooleanField(default=False)
    public          = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.repository_name)
