from django.contrib.auth.models import User 
from rest_framework import serializers
from .models import Specialties, Doctor, Date

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SpecialtiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialties
        fields = ["name", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["specialities" ,"name"]
        extra_kwargs = {"specialities": {"read_only": True}}

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ["doctor", "name", "date_now",  "email", "description"]
        extra_kwargs = {"doctor": {"read_only": True}}
