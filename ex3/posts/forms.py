from django import forms
from .models import postar

class PostForm(forms.ModelForm):
    class Meta:
        model = postar
        fields = [
            'texto',
            'autor',
            
        ] 