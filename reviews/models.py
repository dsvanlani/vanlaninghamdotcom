from django.db import models
from ckeditor.fields import RichTextField

class Review(models.Model):

    body = RichTextField(blank=True, null=True)
    bookTitle = models.CharField(max_length=256, null=False)
    bookAuthor = models.CharField(max_length=64, null=False)
    thumbnail = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return f'{self.bookTitle}'

class Comment(models.Model):

    commenterName = models.CharField(max_length=64, null=False)
    commenterEmail = models.EmailField()
    commentBody = models.TextField(null=False)
    parentReview = models.ForeignKey('review', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
