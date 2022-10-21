from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

import reviews
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from ..reviews.models import Review

# Create your views here.
@login_required
def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        profile_ = Profile()
        if form.is_valid():
            user = form.save()
            profile_.user = user
            profile_.save()
            auth_login(request, user)  # 회원가입과 동시에 로그인을 시키기 위해
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect("accounts:index")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:login")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context=context)


@login_required
def profile(request):
    user_ = request.user
    reviews = user_.review_set.all()
    comments = user_.comment_set.all()
    profile_ = user_.profile_set.all()[0]
    context = {
        "reviews": reviews,
        "comments": comments,
        "profile": profile_,
    }
    return render(request, "accounts/profile.html", context)


@login_required
def profile_update(request):
    user_ = get_user_model().objects.get(pk=request.user.pk)
    current_user = user_.profile_set.all()[0]
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=current_user)
    context = {
        "profile_form": form,
    }
    return render(request, "accounts/profile_update.html", context)


# def channel(request, article_pk):
#     review = Review.objects.get(pk=article_pk)
#     context = {
#         "review": review,
#     }
#     return render(request, "accounts/channel.html", context)
