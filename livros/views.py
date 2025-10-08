from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Livro, Autor, Categoria, Tag, Editora
from .forms import LivroForm, AutorForm, CategoriaForm, TagForm, EditoraForm

# ----------------------------
# VIEWS DE AUTENTICAÇÃO
# ----------------------------

def cadastrar_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/signup.html', {'form': form}) 


def login_view(request):
    next_url = request.GET.get('next', 'livro_list')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            if user.is_staff:
                return redirect('/livros/')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form}) 


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da conta com sucesso.")
    return redirect('login')


# ----------------------------
# VIEWS DE LIVROS (CRUD)
# ----------------------------

class LivroListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = 'livros/listar_livros.html' 
    context_object_name = 'livros'
    login_url = 'login'
    redirect_field_name = 'next'


class LivroCreateView(LoginRequiredMixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livros/criar_livro.html' 
    success_url = reverse_lazy('livro_list')
    login_url = 'login'
    redirect_field_name = 'next'

    def form_valid(self, form):
        messages.success(self.request, "Livro cadastrado com sucesso!")
        return super().form_valid(form)


class LivroUpdateView(LoginRequiredMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livros/atualizar_livro.html' 
    success_url = reverse_lazy('livro_list')
    login_url = 'login'
    redirect_field_name = 'next'

    def form_valid(self, form):
        messages.success(self.request, "Livro atualizado com sucesso!")
        return super().form_valid(form)


class LivroDeleteView(LoginRequiredMixin, DeleteView):
    model = Livro
    template_name = 'livros/deletar_livro.html' 
    success_url = reverse_lazy('livro_list')
    login_url = 'login'
    redirect_field_name = 'next'

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Livro excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

# ----------------------------
# VIEWS DE AUTORES (CRUD)
# ----------------------------

class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name = 'autores/listar_autores.html' 
    context_object_name = 'autores'
    login_url = 'login'

class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/criar_autor.html' 
    success_url = reverse_lazy('autor_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Autor cadastrado com sucesso!")
        return super().form_valid(form)

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/atualizar_autor.html' # 
    success_url = reverse_lazy('autor_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Autor atualizado com sucesso!")
        return super().form_valid(form)

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = 'autores/deletar_autor.html' 
    success_url = reverse_lazy('autor_list')
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Autor excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
 
 
# ----------------------------
# VIEWS DE Categorias (CRUD)
# ----------------------------   
class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categorias/listar_categoria.html' 
    context_object_name = 'categorias'
    login_url = 'login'
    redirect_field_name = 'next'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/criar_categoria.html' 
    login_url = 'login'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Nova Categoria"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Categoria cadastrada com sucesso!")
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/atualizar_categoria.html' # ✅ REUTILIZANDO O MESMO FORMULÁRIO
    success_url = reverse_lazy('categoria_list')
    login_url = 'login'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Categoria"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Categoria atualizada com sucesso!")
        return super().form_valid(form)

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categorias/deletar_categoria.html' 
    success_url = reverse_lazy('categoria_list')
    login_url = 'login'
    redirect_field_name = 'next'
    context_object_name = 'categoria'

    def form_valid(self, form):
        messages.success(self.request, "Categoria excluída com sucesso!")
        return super().form_valid(form)



# ----------------------------
# VIEWS DE Tag(CRUD)
# ----------------------------  

class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tags/listar_tag.html'
    context_object_name = 'tags'
    login_url = 'login'


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tags/criar_tag.html'
    success_url = reverse_lazy('tag_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Tag cadastrada com sucesso!")
        return super().form_valid(form)


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tags/atualizar_tag.html'
    success_url = reverse_lazy('tag_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Tag atualizada com sucesso!")
        return super().form_valid(form)


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tags/deletar_tag.html'
    success_url = reverse_lazy('tag_list')
    context_object_name = 'tags'
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Tag excluída com sucesso!")
        return super().form_valid(form)


# ----------------------------
# VIEWS DE EDITORA (CRUD)
# ----------------------------

class EditoraListView(LoginRequiredMixin, ListView):
    model = Editora
    template_name = 'editoras/listar_editora.html'
    context_object_name = 'editoras'
    login_url = 'login'


class EditoraCreateView(LoginRequiredMixin, CreateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'editoras/criar_editora.html'
    success_url = reverse_lazy('editora_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Editora cadastrada com sucesso!")
        return super().form_valid(form)


class EditoraUpdateView(LoginRequiredMixin, UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'editoras/atualizar_editora.html'
    success_url = reverse_lazy('editora_list')
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Editora atualizada com sucesso!")
        return super().form_valid(form)


class EditoraDeleteView(LoginRequiredMixin, DeleteView):
    model = Editora
    template_name = 'editoras/excluir_editora.html'
    success_url = reverse_lazy('editora_list')
    context_object_name = 'editoras'
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, "Editora excluída com sucesso!")
        return super().form_valid(form)