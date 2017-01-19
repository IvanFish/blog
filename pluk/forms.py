from django import forms
from .models import Article, Comment, UserProfile
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)
        
# Модель формы обратной связи
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)