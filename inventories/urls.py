from django.urls import path
from . import views

app_name = "inventories"

urlpatterns = [
	path('inventory-list/', views.inventory_list, name = "list"),


]