from rest_framework import serializers
from myapp.models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['is_active',]