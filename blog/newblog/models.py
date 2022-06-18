from cgitb import text
from turtle import title
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=23)
    text = models.TextField(unique=True, max_length=200)
    author = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(auto_now_add=True)

def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])

def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title

