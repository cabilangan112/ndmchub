from django.contrib import admin

from . models import repo, UploadModel

admin.site.register(repo)
admin.site.register(UploadModel)
# Register your models here.
