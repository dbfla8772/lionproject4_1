from django.contrib import admin
from django.urls import path
from .views import *

app_name = "formBlog"

urlpatterns = [   
    path('<str:id>', detailHtml, name="detailHtml"), 
    path('new/', newHtml, name="newHtml"),
    path('create/', createPost, name="createPost"),
    path('edit/<str:id>', editHtml, name="editHtml"),  
    path('update/<str:id>', upadatePost, name="updatePost"), 
    path('delete/<str:id>', deletePost, name="deletePost"),  
] 
