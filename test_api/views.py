from django.shortcuts import render

# Create your views here.
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class PostsView(ListAPIView):
  authentication_class = (JSONWebTokenAuthentication,) # Don't forget to add a 'comma' after first element to make it a tuple
  permission_classes = (IsAuthenticated,)