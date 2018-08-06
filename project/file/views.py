from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRendere
from .serializers import FileSerializer

from .models import UploadModel
class FileUpload(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'file_add.html'

    def get(self, request, *args, **kwargs):
        file = UploadModel.objects.all()
        serializer = FileSerializer(UploadModel)
        return Response({'serializer': serializer, 'file': file})

    def post(self,request, *args, **kwargs):
        file = UploadModel.objects.all()
        serializer = FileSerializer(UploadModel, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'file': file})
        serializer.save()
        return redirect('file-list')    