from django.contrib.auth.models import User

from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
  """Provide a get method handle for querying a collection of model instances."""
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
    

class SnippetDetail(generics.RetrieveAPIView):
  """Provide a get method handle for querying a single model instance."""
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer