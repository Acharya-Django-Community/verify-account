from django import forms
from .models import Post
from .models import Feedback
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content',]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','email','question'
        ]