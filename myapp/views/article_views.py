from rest_framework import mixins, viewsets

from myapp.serializers.article_serializer import (
    ArticleListSerializer
)
from myapp.models import Article

class ArticleListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleListSerializer
    