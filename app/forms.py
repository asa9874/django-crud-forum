from django import forms
from app.models import Voca, Comment

class VocaForm(forms.ModelForm):
    class Meta:
        model=Voca
        fields=['english_vo','korean_vo','number_vo']
        labels={
            'english_vo':'영어',
            'korean_vo':'한국어',
            'number_vo':'숫자'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        labels={
            'content':'댓글',
        }