from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('adminpanel/news/categories/', views.categories_list, name="categories_list"),
    path('adminpanel/news/categories/export_csv', views.export_csv, name="export_csv"),
    path('adminpanel/news/categories/export_json', views.export_json, name="export_json"),
    path('adminpanel/news/categories/export_excel', views.export_excel, name="export_excel"),
    path('adminpanel/news/categories/import_data', views.import_data, name="import_data"),
    path('adminpanel/news/categories/add/', views.categories_list_add, name="categories_list_add"),
    path('adminpanel/news/categories/delete/<int:pk>/', views.categories_list_delete, name="categories_list_delete"),
    path('adminpanel/news/categories/edit/<int:pk>/', views.categories_list_edit, name="categories_list_edit"),
]