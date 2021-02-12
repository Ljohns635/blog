from django.shortcuts import render
from blog_app.models import BlogItem, Author

def homepage(request):
    articles = BlogItem.objects.all()
    context = {'heading': 'Latisha Shanice', 'articles': articles}
    return render(request, 'home_page.html', context)
