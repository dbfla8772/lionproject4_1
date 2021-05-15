from django.contrib import admin
from django.urls import path
from .views import *

app_name = "formBlog"

urlpatterns = [   
    path('<str:id>', detailHtml, name="detailHtml"), 
    path('new/', new, name="new"),
    path('edit/<str:id>', edit, name="edit"),  
    path('delete/<str:id>', deletePost, name="deletePost"),  
] 
