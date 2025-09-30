from django.contrib import admin
from .models import Autor, Editora, Categoria, Livro, Emprestimo


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'data_nascimento')
    search_fields = ('nome', 'nacionalidade')
    list_filter = ('nacionalidade',)
    ordering = ('nome',)


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado')
    search_fields = ('nome', 'cidade', 'estado')
    list_filter = ('estado',)
    ordering = ('nome',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editora', 'categoria', 'ano_publicacao', 'isbn')
    search_fields = ('titulo', 'autor_nome', 'editora_nome', 'isbn')
    list_filter = ('categoria', 'editora', 'ano_publicacao')
    ordering = ('titulo',)
    autocomplete_fields = ('autor', 'editora', 'categoria')  # 🔍 autocomplete em campos ForeignKey


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_emprestimo', 'data_devolucao')
    search_fields = ('livro_titulo', 'usuario_username')
    list_filter = ('data_emprestimo', 'data_devolucao')
    date_hierarchy = 'data_emprestimo'
    ordering = ('-data_emprestimo',)