from django.urls import path

from . import views
from .views import Profile
app_name = 'user'
urlpatterns = [
#	path('user', Profile.as_view(), name='profile'),
]