from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'poster', 'description', 'release_date', 'actors', 'category', 'youtube_link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'poster': forms.ImageField(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.TextInput(attrs={'class': 'form-control'}),
            'actors': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'youtube_link': forms.TextInput(attrs={'class': 'form-control'}),

        }

