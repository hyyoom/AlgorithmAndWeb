# 사용자에게 입력받기 위한 양식을 만들어주는 클래스 작성
from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField()

# Form에 포함되어야 할 요소를 직접 선언이 아니라 Model에서 참조하도록 함

# Model + Form의 역할을 하는 class~
class ArticleForm(forms.ModelForm):
    class Meta: #data를 설명하기위한 데이터
        model = Article
        fields = ['title', 'content']
        # fields = '__all__'