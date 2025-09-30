from django import forms
from .models import Livro


# Formulário baseado no Models
# Cria os campos automaticamente

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro             # Modelo que vai ser usado no formulário
        fields = '__all__'        # Inclui todos os campos do modelo



  