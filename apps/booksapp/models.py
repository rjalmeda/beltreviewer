from __future__ import unicode_literals

from django.db import models
from ..mylogin.models import Users

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class BookReviews(models.Model):
    FK_userid = models.ForeignKey(Users, related_name='review_user')
    FK_book = models.ForeignKey(Book, related_name='review_book')
    review = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    