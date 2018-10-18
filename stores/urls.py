from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
	path('store-list/', views.store_list, name = "list"),

]