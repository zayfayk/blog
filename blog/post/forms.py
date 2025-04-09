from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}))

    class Meta:
        model = Post
        fields = ('title', 'Body', 'author', 'category')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'Body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
        }

class EditForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}))

    class Meta:
        model = Post
        fields = ('title', 'Body', 'category')  # Ensure 'category' is included
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'Body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
        }

class DeleteForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}))

    class Meta:
        model = Post
        fields = ['title', 'Body', 'author', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'Body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
        }
