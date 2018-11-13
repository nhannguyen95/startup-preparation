from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListAPIView):
  """Provide a get method handle for querying a collection of model instances."""
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveAPIView):
  """Provide a get method handle for querying a single model instance."""
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer