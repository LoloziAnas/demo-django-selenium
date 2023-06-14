from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("/scrape_data",views.scape_data,name="scrape_data")
]