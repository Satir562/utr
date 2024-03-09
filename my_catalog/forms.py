from .models import Story
from django.forms import ModelForm, TextInput, Textarea

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'summary', 'content']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),

            'summary': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое содержание'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            })
        }