from rest_framework import serializers
from .models import Article


# Create your models here.
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'