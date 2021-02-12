from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=50)
    byline = models.TextField()

    def __str__(self):
        return self.name

class BlogItem(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    post_date = models.DateTimeField(timezone.now())
    body = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.author}"
