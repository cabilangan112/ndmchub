from django.db import models
from repo.models import repo
from django.db import models
from django.core.files.storage import FileSystemStorage
#fs = FileSystemStorage(location=PRIVATE_DIR)

class UploadModel(models.Model):
    repository_name = models.ForeignKey(repo,on_delete=models.CASCADE)
    File_name       = models.CharField(max_length=150)
    file            = models.FileField(upload_to='static/file')
    description     = models.TextField(null=True, blank=True)
    date            = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now_add=True)
    update_changes  = models.CharField(max_length=150,null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.File_name)
