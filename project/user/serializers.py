from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models import Account, org, info

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )

class OrgSerializer(serializers.ModelSerializer):
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = org
        fields = (
          'org_name',
          'description',
          'timesince',
          'date_created',
          'date_modified',
          'private',
          'public',
        )

    def get_date_modified(self, instance):
        return instance.date.strftime("%b %d, %Y | at %I:%M %p")

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields = (
          'account',
          'profile_picture',
          'first_name',
          'last_name'
          'tagline',
          'sex',
          'age',
          'Location',
          'Bio',
          'student',
          'teacher',
          'office',
        )



class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                'last_name',  'date_of_birth ', 'password', 
                  'confirm_password',)
        read_only_fields = ('created_at', 'updated_at',)

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.tagline = validated_data.get('tagline', instance.tagline)
            instance.save()
            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)
            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()
            update_session_auth_hash(self.context.get('request'), instance)
            return instance