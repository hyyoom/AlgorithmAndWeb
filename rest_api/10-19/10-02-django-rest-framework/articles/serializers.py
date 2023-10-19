from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)



class CommetSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer): # 새로 정의하는거라 이름 겹쳐도 됨
        class Meta:
            model = Article
            fields = ('title',)

    article = ArticleSerializer(read_only=True)
    # 밑에 원래 있던 read_only랑 겹쳐져서 안먹으니까 여기 안에 넣어줘야함

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)



class ArticleSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('content',)

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count')
    # source부분에 원래 썻듯이 article.comment_set.count()같이 뒤에 함수 넣어주면 됨.
    class Meta:
        model = Article
        fields = '__all__'