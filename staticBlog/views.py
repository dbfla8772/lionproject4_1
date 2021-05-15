from django.shortcuts import render, redirect, get_object_or_404  #404는 서버가 요청한 페이지를 찾을 수 없다.
from formBlog.models import Blog

# Create your views here.
def homeHtml(request):
    blogObject = Blog.objects.all    # Blog 클래스에 있는 모든 객체를 불러와서 저장
    return render(request, 'home.html', {'blogObject':blogObject})