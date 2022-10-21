from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("<int:review_pk>/comments/", views.comment_create, name="comment_create"),
    path(
        "<int:review_pk>/comments/<int:comment_pk>/delete/",
        views.delete_create,
        name="delete_create",
    ),
]