from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Video, Rating, GpuStatus
from .serializers import VideoSerializer, RatingSerializer, UserSerializer, GpuStatusSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


# Create your views here.
# class GpuStatusViewSet(viewsets.ModelViewSet):
#     queryset = GpuStatus.objects.raw('SELECT * FROM gpu_monitoring_article  where (id,server_name ) IN  (SELECT MAX(id,server_name ) FROM gpu_monitoring_article group by(server_name)) group by server_name
#     serializer_class = GpuStatusSerializer
#     authentication_class = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     print(queryset)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
