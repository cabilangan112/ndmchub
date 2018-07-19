from django.db import models

class UploadModel(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    update_changes = models.CharField(max_length=150)
    description     = models.TextField()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.repository_name)
