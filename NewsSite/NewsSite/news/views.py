from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import News, Author

def home(request):
    recent_articles = News.objects.all().order_by('-publication_date')[:6]
    return render(request, 'news/home.html', {'recent_articles': recent_articles})

def all_news(request):
    complete_news_list = News.objects.all().order_by('-publication_date')
    return render(request, 'news/all_news.html', {'complete_news_list': complete_news_list})

def news_detail(request, article_id):
    selected_article = get_object_or_404(News, id=article_id)
    return render(request, 'news/news_details.html', {'article': selected_article})

def authors_list(request):
    authors = Author.objects.all()  # Fetch all authors from the database
    return render(request, 'news/authors.html', {'authors': authors})  # Pass authors to the template

def author_news(request, writer_id):
    selected_author = get_object_or_404(Author, pk=writer_id)
    articles_by_author = News.objects.filter(author=selected_author).order_by('-publication_date')
    return render(request, 'news/author_news.html', {'selected_author': selected_author, 'articles_by_author': articles_by_author})

def author_articles(request, author_id):
    """New function to display articles by a specific author."""
    selected_author = get_object_or_404(Author, id=author_id)
    articles = News.objects.filter(author=selected_author).order_by('-publication_date')
    return render(request, 'news/author_articles.html', {'author': selected_author, 'articles': articles})

class AllNewsView(ListView):
    model = News
    template_name = 'news/all_news.html'  # Make sure this matches your template path
    context_object_name = 'news_list'  # This should match the variable in your template
