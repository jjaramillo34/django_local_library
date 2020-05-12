from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('adminpanel/news/subcategories/', views.subcategories_list, name="subcategories_list"),
    path('adminpanel/news/subcategories/<slug>', views.subcategories_list_by_subcat, name="subcategories_list_by_subcat"),
    path('adminpanel/news/subcategories/add/', views.subcategories_list_add, name="subcategories_list_add"),
    path('adminpanel/news/subcategories/delete/<int:pk>/', views.subcategories_list_delete, name="subcategories_list_delete"),
    path('adminpanel/news/subcategories/view/', views.subcategories_list_view, name="subcategories_list_view"),
    path('adminpanel/news/subcategories/edit/', views.subcategories_list_edit, name="subcategories_list_edit"),
]