from django.contrib import admin
from blog_app.models import BlogItem, Author, SubscribePage, SuggestPage

admin.site.register(Author)
admin.site.register(BlogItem)
admin.site.register(SubscribePage)
admin.site.register(SuggestPage)
