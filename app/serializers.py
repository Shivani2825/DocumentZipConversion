# serializers.py
from rest_framework import serializers
from .models import Person, Files
from rest_framework.validators import UniqueValidator


class PersonSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=Person.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Person
        fields = '__all__'


class PersonLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'
