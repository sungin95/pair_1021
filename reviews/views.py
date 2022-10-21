from django.shortcuts import render, redirect
from .models import Reveiw, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def comment_create(request, review_pk):
    review = Reveiw.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect("reviews:detail", review_pk)
