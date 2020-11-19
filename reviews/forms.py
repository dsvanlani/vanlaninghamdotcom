from django import forms
from .models import Review, BioPicture



class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'bookTitle',
            'bookAuthor',
            'thumbnail',
            'body'
        ]


class ChangeBioPictureForm(forms.ModelForm):

    class Meta:
        model = BioPicture
        fields = [
            'image',
            'altText',
            'caption',
        ]