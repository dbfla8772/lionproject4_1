from django.urls import path
from .views import * 
from formBlog.views import detailHtml, new

urlpatterns = [    
    path('<str:id>', detailHtml, name="detailHtml"), 
    path('new/', new, name="new"), 
] 