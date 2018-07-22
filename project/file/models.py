from django.db import models

 
class UploadModel(models.Model):
    File_name = models.CharField(max_length=150)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    description     = models.TextField(null=True, blank=True)
    date            = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now_add=True)
    update_changes  = models.CharField(max_length=150,null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.File_name)
