from django.urls import path
from .views import homePage

# create urls routes for home app and link to main apps urls routes
urlpatterns = [
    path("",homePage,name="homePage")
]
