from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("", views.david, name="david"),
    path("<str:name>",views.greet, name="greet")
]