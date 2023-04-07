from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CompanySerializer
# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer