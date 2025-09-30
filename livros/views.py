from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Livro
from .forms import LivroForm

# View para listar todos os livros cadastrados
class LivroListView(ListView):
    model = Livro
    template_name = 'livros/listar_livros.html'
    context_object_name = 'livros'


# View para criar um novo livro
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livros/criar_livro.html' 
    success_url = reverse_lazy('livro_list')


# View para editar um livro já existente
class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livros/atualizar_livro.html' 
    success_url = reverse_lazy('livro_list')


# View para excluir um livro
class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livros/deletar_livro.html' 
    success_url = reverse_lazy('livro_list')