from django.contrib.auth.models import User, Group

from django.utils.timesince import timesince
from rest_framework import serializers
from .models import UploadModel
from repo.models import repo
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadModel
        fields = (
            'repository_name',
            'File_name',
            'description',
            'date',
            'date_modified',
            'update_changes',
            )
        def validate(self, validated_data):
            validated_data['repository_name'] = self.context['request'].repo
            validated_data['name'] =     os.path.splitext(validated_data['file'].File_ame)[0]
            validated_data['size'] = validated_data['file'].size
            #other validation logic
            return validated_data

        def create(self, validated_data):
            return FileUploader.objects.create(**validated_data)