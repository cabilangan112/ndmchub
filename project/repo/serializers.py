from django.contrib.auth.models import User, Group
from django.utils.timesince import timesince
 
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = repo
        fields = (
        	'owner',
        	'repository_name',
        	'description',
        	'date_created',
        	'date_modified',
        	'private',
        	'public',
        	)