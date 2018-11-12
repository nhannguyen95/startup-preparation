from rest_framework import viewsets
from rest_framework import permissions

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
