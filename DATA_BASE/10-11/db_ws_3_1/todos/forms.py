from django import forms
from .models import Todo


class TodoFrom(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'complete',)
