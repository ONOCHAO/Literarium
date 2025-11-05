from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
