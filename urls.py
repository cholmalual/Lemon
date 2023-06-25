from django.urls import path
from . import views

#app_name = 'menu'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('<int:item_id>/', views.menu_item, name='menu_item'),
    # Add other URL patterns if necessary
]
