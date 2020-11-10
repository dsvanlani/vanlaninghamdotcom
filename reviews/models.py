from django.db import models

class Review(models.Model):

    bookISBN = models.CharField(max_length=13, null=False)
    content = models.FileField(null=False, upload_to='reviews/')
    bookTitle = models.CharField(max_length=256, null=False)
    bookAuthor = models.CharField(max_length=64, null=False)
    thumbnail = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return f'{self.bookTitle} - {self.bookISBN}'

class Comment(models.Model):

    commenterName = models.CharField(max_length=64, null=False)
    commenterEmail = models.EmailField()
    commentBody = models.TextField(null=False)
    parentReview = models.ForeignKey('review', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
