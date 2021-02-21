from django import forms
from .models import *



class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'bookTitle',
            'bookAuthor',
            'bookAuthorLastName',
            'thumbnail',
            'body'
        ]

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = [
            'articleTitle',
            'body',
        ]

class ChangeBioPictureForm(forms.ModelForm):

    class Meta:
        model = BioPicture
        fields = [
            'image',
            'altText',
            'caption',
        ]

class ChangeBioParagraphForm(forms.ModelForm):

    class Meta:
        model = BioParagraph
        fields = [
            'text'
        ]
