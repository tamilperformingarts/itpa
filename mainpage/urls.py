from django.urls import path
from . import views

app_name = "mainpage"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path("tamilisai/", views.tamilisai, name="tamilisai"),
    path("tamilisai_events/", views.tamilisai_events, name="tamilisai_events"),
    path("textbook/", views.textbook, name="textbook"),
    path("parai/", views.parai, name="parai"),
    path("pg/", views.pg, name="pg"),
    path("silambam/", views.silambam, name="silambam"),
    path("sg/", views.sg, name="sg"),
]
