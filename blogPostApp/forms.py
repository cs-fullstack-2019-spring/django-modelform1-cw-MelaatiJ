from django import forms
from .models import BlogPost

# model from that shows only the text and title field
class NewBlogPost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]