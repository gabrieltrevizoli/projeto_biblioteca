from django.urls import path
from .views import (
    LivroListView,
    LivroCreateView,
    LivroUpdateView,
    LivroDeleteView,
)

urlpatterns = [
    path('', LivroListView.as_view(), name='livro_list'),
    path('novo/', LivroCreateView.as_view(), name='livro_create'),
    path('<int:pk>/editar/', LivroUpdateView.as_view(), name='livro_update'),
    path('<int:pk>/excluir/', LivroDeleteView.as_view(), name='livro_delete'),
]