from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="my_index"),
    path('shows/', views.shows, name="my_shows"),
    path('shows/new/', views.new, name="my_new"),
    path('shows/<int:show_id>/edit/', views.edit, name="my_edit"),
    path('shows/<int:show_id>/update/', views.update, name="my_update"),
    path('shows/<int:show_id>/destroy/', views.destroy, name="my_destroy"),
    path('shows/<int:show_id>/', views.view, name="my_view"),
    path('shows/create/', views.create, name="my_create"),
]