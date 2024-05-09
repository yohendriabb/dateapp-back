from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics
from .models import Specialties, Doctor, Date

from .serializers import UserSerializer , SpecialtiesSerializer, DoctorSerializer, DateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class CreateUserview(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class SpecialtiesListCreate(generics.ListCreateAPIView):
    serializer_class = SpecialtiesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): 
        user = self.request.user
        return Specialties.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class SpecialtiesDelete(generics.DestroyAPIView):
    serializer_class = SpecialtiesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): 
        user = self.request.user
        return Specialties.objects.filter(author=user)

