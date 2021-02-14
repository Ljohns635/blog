from django.shortcuts import render
from blog_app.models import BlogItem, Author, SubscribePage, SuggestPage
from blog_app.forms import SubscribePageForm, SuggestPageForm

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
    context = {}
    if request.method == 'POST':
        form = SuggestPageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = SuggestPage.objects.create(
                full_name = data['full_name'],
                email = data['email'],
                subject = data['subject'],
                body = data['body']
            )
            context.update({'message':'Submitted successfully!'})
    form = SuggestPageForm()
    context.update({'form': form, 'heading': 'Latisha Shanice'})
    return render(request, 'suggest.html', context)

def subscribe(request):
    context = {}
    if request.method == 'POST':
        form = SubscribePageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = SubscribePage.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
            )
            context.update({'message':'Submitted successfully!'})
    form = SubscribePageForm()
    context.update({'form': form, 'heading': 'Latisha Shanice'})
    return render(request, 'subscribe.html', context)

def about(request):
    auth_info = Author.objects.all()
    context = {'auth_info': auth_info, 'heading': 'Latisha Shanice'}
    return render(request, 'about.html', context)
