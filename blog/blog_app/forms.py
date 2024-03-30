from django import forms
from .models import Blog



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'media']

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['media'].required = False  

    def save(self, commit=True):
        blog = super(BlogForm, self).save(commit=False)
        if commit:
            blog.save()
        return blog


class BlogPostUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content','media']


