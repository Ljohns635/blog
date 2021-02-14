from django.shortcuts import render
from blog_app.models import BlogItem, Author

def homepage(request):
    articles = BlogItem.objects.all()
    context = {'heading': 'Latisha Shanice', 'articles': articles}
    return render(request, 'home_page.html', context)

def article(request, post_id):
    article = BlogItem.objects.get(id=post_id)
    context = {'article': article, 'heading': 'Latisha Shanice'}
    return render(request, 'article.html', context)

def blogger(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    articles = BlogItem.objects.filter(author=author_obj)
    context = {'author': author_obj, 'articles': articles, 'heading': 'Latisha Shanice'}
    return render(request, 'author.html', context)

def categories(request):
    categorys = BlogItem.objects.all()
    context = {'list': 'This is the categories page', 'heading': 'Latisha Shanice', 'categorys': categorys}
    return render(request, 'categories.html', context)

def suggestions(request):
    context = {'form': 'This is the suggestions form page', 'heading': 'Latisha Shanice'}
    return render(request, 'suggest.html', context)

def subscribe(request):
    context = {'form': 'Subscribe to my blog page', 'heading': 'Latisha Shanice'}
    return render(request, 'subscribe.html', context)

def about(request):
    context = {'about': 'About me page', 'heading': 'Latisha Shanice'}
    return render(request, 'about.html', context)
