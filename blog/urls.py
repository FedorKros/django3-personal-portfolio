from django.urls import path
from portfolio import views
from . import views
from django.conf.urls import include

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
