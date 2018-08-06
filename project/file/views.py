from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

from .models import UploadModel
class FileUpload(APIView):
    
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data )
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        file = [file.File_name for file in UploadModel.objects.all()]
        return Response(file) 