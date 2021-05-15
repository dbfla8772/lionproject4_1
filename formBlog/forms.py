from django import forms
from .models import Blog

class BlogForm(forms.ModelForm): # 장고에서 지원해주는 forms를 상솓받음
    class Meta: # Blog 모델에 필드를 연결, 이 정보로 BlogForm을 만들어줌. (이름표 역할)
        model = Blog
        fields = ['title', 'writer', 'body', 'image'] # pub_date 빼고는 전부 받아야 함.