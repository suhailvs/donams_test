from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajx/', views.ajax_showpage, name='ajax_showpage'),
    path('ajx/add/', views.ajax_adduser, name='ajax_adduser'),
    path('ajx/delete/', views.ajax_deleteuser, name='ajax_deleteuser'),
    
]
