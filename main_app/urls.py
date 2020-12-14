from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('scooters/', views.scooters_index, name='index'),
  path('scooters/<int:scooter_id>/', views.scooters_detail, name='detail'),
  path('scooters/create/', views.ScooterCreate.as_view(), name='scooters_create'),
  path('scooters/<int:pk>/update/', views.ScooterUpdate.as_view(), name='scooters_update'),
  path('scooters/<int:pk>/delete/', views.ScooterDelete.as_view(), name='scooters_delete'),
  path('scooters/<int:scooter_id>/add_service/', views.add_service, name='add_service'),
  # associate a part with a scooter (M:M)


]