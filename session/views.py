from django.shortcuts import render

from session.serializers import SessionSerializer
from session.serializers import StudentSerializer
from .models import Session
from .models import Student
from .serializers import SessionSerializer
from .serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SessionViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer