from django import forms
from .models import Livro, Autor, Categoria, Tag, Editora

#forms livro , autor, categoria, tag, editora

# Forms dos Livros
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo', 
            'autor', 
            'editora', 
            'categoria', 
            'ano_publicacao',  
            'isbn',            
            'tags'
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(), 
        }

# Forms de Autores
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade', 'data_nascimento']
       
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }
    
    
# Forms de Categorias    
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
        
        fields = ['nome', 'cidade', 'estado'] 
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da editora'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
        }