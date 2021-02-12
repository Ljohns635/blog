from django.contrib import admin
from blog_app.models import BlogItem, Author

admin.site.register(Author)
admin.site.register(BlogItem)
