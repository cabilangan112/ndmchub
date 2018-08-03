from django.urls import path

from . import views
from .views import FileUpload
app_name = 'file'
urlpatterns = [
	path('upload', FileUpload.as_view(), name='file-upload'),
]