from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta: #tell Django which model to use to create form
        model = Postfields = ('title', 'text',)