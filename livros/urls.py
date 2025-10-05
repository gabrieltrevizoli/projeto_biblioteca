from django.urls import path
from .views import (
    login_view,
    logout_view,
    cadastrar_view,
    
    LivroListView,
    LivroCreateView,
    LivroUpdateView,
    LivroDeleteView,
    
    AutorListView,
    AutorCreateView,
    AutorUpdateView,
    AutorDeleteView,
    
    CategoriaListView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    
    TagCreateView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    
    EditoraCreateView,
    EditoraListView,
    EditoraUpdateView,
    EditoraDeleteView,
)

urlpatterns = [
    
    # Urls de Autenticação
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', cadastrar_view, name='signup'),

    # Urls de Livros
    path('', LivroListView.as_view(), name='livro_list'),
    path('novo/', LivroCreateView.as_view(), name='livro_create'),
    path('<int:pk>/editar/', LivroUpdateView.as_view(), name='livro_update'),
    path('<int:pk>/excluir/', LivroDeleteView.as_view(), name='livro_delete'),
    
    # Urls de Autores
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/novo/', AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<int:pk>/excluir/', AutorDeleteView.as_view(), name='autor_delete'),
    
    # Urls de Categorias
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nova/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/excluir/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    
    # URLs de Tags
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/nova/', TagCreateView.as_view(), name='tag_create'),
    path('tags/editar/<int:pk>/', TagUpdateView.as_view(), name='tag_update'),
    path('tags/excluir/<int:pk>/', TagDeleteView.as_view(), name='tag_delete'),
    
    # URLs de Editoras
    path('editoras/', EditoraListView.as_view(), name='editora_list'),
    path('editoras/nova/', EditoraCreateView.as_view(), name='editora_create'),
    path('editoras/editar/<int:pk>/', EditoraUpdateView.as_view(), name='editora_update'),
    path('editoras/excluir/<int:pk>/', EditoraDeleteView.as_view(), name='editora_delete'),

]