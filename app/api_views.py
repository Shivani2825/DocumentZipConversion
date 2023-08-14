# api_views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person, Files
from django.contrib.auth.hashers import make_password, check_password
from .serializers import PersonSerializer, FilesSerializer, PersonLoginSerializer

class PersonRegistrationAPI(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        password = self.request.data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

class PersonLoginAPI(generics.CreateAPIView):
    serializer_class = PersonLoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Person.objects.get(email=email)
            if check_password(password, user.password):
                return Response({"detail": "Authentication successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Person.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class FilesUploadAPI(generics.CreateAPIView):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
 
  