from django.urls import path
from . import views
from .views import AllNewsView

urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка
    path('news/', AllNewsView.as_view(), name='news_list'),  # Список новин
    path('news/<int:article_id>/', views.news_detail, name='news_detail'),  # Деталі новини
    path('authors/', views.authors_list, name='authors'),  # Список авторів
    path('authors/<int:writer_id>/', views.author_news, name='author_news'),  # Новини автора
    path('authors/<int:author_id>/', views.author_articles, name='author_articles'),  # Статті автора
]