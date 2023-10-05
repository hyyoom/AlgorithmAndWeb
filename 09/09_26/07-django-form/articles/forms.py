from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
    



class ArticleForm(forms.ModelForm):
    # model 등록
    class Meta: # 꼭 메타
        model = Article
        fields = '__all__'
        # fields = ('title,')
