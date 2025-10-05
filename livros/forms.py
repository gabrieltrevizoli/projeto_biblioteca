from django import forms
from .models import Livro, Autor, Categoria, Tag, Editora


# Forms de Livros
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro            # Modelo que vai ser usado no formulário
        fields = '__all__'       # Inclui todos os campos do modelo


# Forms de Autores
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade', 'data_nascimento']
        # Adicionando classes do Bootstrap e um widget de data para melhorar a aparência
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }
    
    
# Forms de Catgorias    
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Ficção Científica'}),
        }
        
# Forms de Tags

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Romance'}),
        }
        
# Forms de Editoras

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        # Remova 'site' da lista
        fields = ['nome', 'cidade', 'estado'] # ou apenas os campos que quer no form
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da editora'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
        }