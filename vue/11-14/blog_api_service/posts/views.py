from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer

# Create your views here.
@api_view(['GET'])
def postlist(request):
    posts = get_list_or_404(Post)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def categorycreate(request):
    if request.method == 'GET':
        categorys = get_list_or_404(Category)
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)
    else:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)