from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.
@api_view(['GET'])
def todos(request):
    todos = get_list_or_404(Todo)
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)