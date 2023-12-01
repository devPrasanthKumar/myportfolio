from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact/", views.SendEmailView.as_view(), name="contact"),

]
