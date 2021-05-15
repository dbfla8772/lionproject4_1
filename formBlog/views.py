from django.shortcuts import render, redirect, get_object_or_404  #404는 서버가 요청한 페이지를 찾을 수 없다.
from django.utils import timezone   
from .models import Blog
from .forms import BlogForm

# Create your views here.
def homeHtml(request):
    blogObject = Blog.objects.all    # Blog 클래스에 있는 모든 객체를 불러와서 저장
    return render(request, 'home.html', {'blogObject':blogObject})

def detailHtml(request, id):
    blogModel = get_object_or_404(Blog, pk = id)  # pk = Primary Key (데이터베이스의 식별자), Table의 row 하나하나를 구별하는 ID값
    return render(request, 'detail.html', {'blogModel':blogModel})

def new(request):  #new.html을 보여줌.
    if request.method == 'POST':
        post_form = BlogForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)  # 임시저장
            new_post.pub_date = timezone.now()
            new_post.save()
            return redirect('homeHtml')
    else:
        post_form = BlogForm()
        return render(request, 'new.html', {'post_form':post_form})

def edit(request, id):  # edit.html을 보여줌. 
    edit_post = get_object_or_404(Blog, pk=id)
    if request.method == 'GET':
        post_form = BlogForm(instance = edit_post)
        return render(request, 'edit.html', {'blogEdit':post_form})
    else:
        post_form = BlogForm(request.POST, request.FILES, instance = edit_post)
        if post_form.is_valid():
            edit_post = post_form.save(commit=False)  # 임시저장
            edit_post.pub_date = timezone.now()
            edit_post.save()
            return redirect('detailHtml', edit_post.id)        # 기능을 사용하고 원래 페이지로 돌아가야함. redirect 사용, 새로운 객체의 id를 보내줘야함.

def deletePost(request, id):    # 보내주는 id 값의 데이터를 삭제하는 함수  
    delete_post = Blog.objects.get(id=id)
    delete_post.delete()
    return redirect('homeHtml') # home.html로 이동