from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    # urls for views
    path('news/<slug>/', views.news_detail, name='news_detail'),
    # urls for adminpanel profile
    path('adminpanel/news/profile/', views.profile, name='profile'),
    path('adminpanel/news/profile/#settings/', views.add_news_profile, name='add_news_profile'),
    # urls for adminpanel edit
    path('adminpanel/news/list/edit/<int:pk>/', views.edit_news, name='edit_news'),
    # urls for adminpanel list
    path('adminpanel/news/list/', views.news_list, name='news_list'),
    path('adminpanel/news/list/test_update', views.test_update, name='test_update'),
    path('adminpanel/news/list/delete/<int:pk>/', views.news_delete, name='news_delete'),

    url(r'^adminpanel/news/add/$', views.add_news, name='add_news'),
    url(r'^adminpanel/news/tables/$', views.tables, name='tables'),
]