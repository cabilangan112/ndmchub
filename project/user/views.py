from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from user.serializers import AccountSerializer,InfoSerializer
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import json
from .models import info
from django.contrib.auth import authenticate, login
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

user = get_user_model()

 

class Profile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request, pk):
        profile = info.objects.all()
        serializer = InfoSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(info, pk=pk)
        serializer = InfoSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('/')
