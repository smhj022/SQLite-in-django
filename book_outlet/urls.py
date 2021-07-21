from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page" ),
    path("<slug:slug>", views.book_details, name="book_details")
]
