from django import forms
from apps.avaliacoes.models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        widgets = {
            'data_criacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }