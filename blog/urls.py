from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_main_view, name= "main"),
    path('<int:pid>/', single_blog_view, name= "single"),
    path('category/<str:cat_name>/', blog_main_view, name= "category"),
    path('test',test_view , name='test')
]