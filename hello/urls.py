from django.urls import path
from hello import views


urlpatterns = [
    # path("", home_list_view, name="home"),
    path("", views.search, name="search"),
    # path("search/", views.search, name="search"),
]
