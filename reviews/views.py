from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def index(request):
    pass

def detail(request, pk):
    pass

def create(request):
    pass

def update(request, pk):
    pass

def delete(request, pk):
    pass

@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect("reviews:detail", review_pk)


def delete_create(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        messages.warning(request, "댓글이 삭제되었습니다.")
    return redirect("reviews:detail", review_pk)
