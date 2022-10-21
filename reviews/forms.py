from django import forms
from .models import Comment, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            "review",
            "user",
        )
