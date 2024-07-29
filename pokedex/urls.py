from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pokemon>/", views.pokemon, name="pokemon"),
    path("add_pokemon", views.add_pokemon, name="add_pokemon"),
    path("pokemon/<int:edit_pokemon>/", views.pokemon, name="pokemon"),
    path("delete_pokemon/<int:id>", views.delete_pokemon, name="delete_pokemon"),
    path("login/", views.CustomLoginView.as_view() , name="login"),
    path("edit_pokemon/<int:id>", views.edit_pokemon, name="edit_pokemon "),
]