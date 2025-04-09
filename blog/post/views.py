from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm
from django.urls import reverse_lazy

def base(request):
    cat_menu = Category.objects.all()  # Fetch all categories
    return render(request, 'base.html', {'cat_menu': cat_menu})  # Pass categories to the template


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)  # Burada HomeView olmalı
        context["cat_menu"] = cat_menu
        context["show_dropdown"] = True  
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cat_menu = Category.objects.all()  # Kategorileri alıyoruz
        context["cat_menu"] = cat_menu  # Kategori menüsünü ekliyoruz
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_add.html'
    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_update.html'

    def get_success_url(self):
        return reverse_lazy('Home')
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delet.html'
    success_url = reverse_lazy('Home')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category.html'
    success_url = reverse_lazy('Home')


def CategoryView(request, cats):
    # Replace '-' with spaces to match the category name
    category_name = cats.replace('-', ' ')
    # Filter the Category object by name
    category = Category.objects.filter(name__iexact=category_name).first()
    if category:
        # Filter posts by the category object
        category_posts = Post.objects.filter(category=category)
    else:
        category_posts = Post.objects.none()  # No posts if category doesn't exist

    cat_menu = Category.objects.all()
    return render(request, 'category_list.html', {
        'cats': category_name.title(),  # Display the category name with title case
        'category_posts': category_posts,
        'cat_menu': cat_menu
    })
