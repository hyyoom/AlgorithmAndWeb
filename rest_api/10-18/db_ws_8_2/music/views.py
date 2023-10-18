from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MusicListSerializers,MusicSerializers
from .models import Music


# 전체 음악 조회
# 음악 생성
@api_view(['GET','POST'])
def music_list(request):
    if request.method=='GET':
        musics = Music.objects.all()
        serializers = MusicListSerializers(musics, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = MusicSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=status.HTTP_201_CREATED)


@api_view(['GET','POST','PUT'])
def music_detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    if request.method=='GET':
        serializers = MusicSerializers(music)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        tmp = music_pk
        music.delete()
        return Response(f'음악 {tmp}번이 삭제되었습니다.',status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        serializers = MusicListSerializers(music,data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=status.HTTP_201_CREATED)






