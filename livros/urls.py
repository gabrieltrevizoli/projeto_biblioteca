from django.urls import path
from .views import LivroListView, LivroCreateView, LivroUpdateView, LivroDeleteView

urlpatterns = [
    path('', LivroListView.as_view(), name='livro_list'),              # listar todos os livros
    path('novo/', LivroCreateView.as_view(), name='livro_create'),     # Form para adicionar novo livro
    path('<int:pk>/editar/', LivroUpdateView.as_view(), name='livro_update'),  # Editar livro existente
    path('<int:pk>/deletar/', LivroDeleteView.as_view(), name='livro_delete'), # Excluir livro existente
]
