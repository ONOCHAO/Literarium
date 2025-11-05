from django.db import models

class Poet(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Poem(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Poet, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
