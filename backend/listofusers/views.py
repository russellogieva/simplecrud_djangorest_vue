from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters

from .models import Users, Role
from .serializers import UsersSerializer, RolesSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RolesSerializer