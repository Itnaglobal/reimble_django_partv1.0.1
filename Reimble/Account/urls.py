from django.urls import path, include
from .views import *

urlpatterns = [
    path("countries/", CountryApiView.as_view()),
    path("professions/", ProfessionsApiView.as_view()),
    path("users/", UserSerializerApiview.as_view()),
]