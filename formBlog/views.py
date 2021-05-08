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

def newHtml(request):  #new.html을 보여줌.
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

def createPost(request):     #new.html의 정보를 받아서 데이터베이스에 저장
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = form.save(commit=False)  # 임시저장
        new_post.pub_date = timezone.now()
        new_post.save()
        return redirect('formBlog:detailHtml', new_post.id)      # 기능을 사용하고 원래 페이지로 돌아가야함. redirect 사용, 새로운 객체의 id를 보내줘야함.
    return redirect('homeHtml')

def editHtml(request, id):  # edit.html을 보여줌. 
    edit_post = Blog.objects.get(id=id) #id 값을 받음.
    return render(request, 'edit.html', {'blogEdit':edit_post})

def upadatePost(request, id):   #id 값을 받음. 기존의 수정해야 할 id 값을 받음. edit.html에서 수정한 내용을 데이터베이스에 적용
    update_post = Blog.objects.get(id=id)
    update_post.title = request.POST['title']  # id 값의 colmn들을 덮어씌워야함.
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']          
    update_post.pub_date = timezone.now()      
    update_post.save()  # 무조건 해야함. 안하면 데이터베이스에 수정이 안됨.
    return redirect('formBlog:detailHtml', update_post.id)      

def deletePost(request, id):    # 보내주는 id 값의 데이터를 삭제하는 함수  
    delete_post = Blog.objects.get(id=id)
    delete_post.delete()
    return redirect('homeHtml') # home.html로 이동