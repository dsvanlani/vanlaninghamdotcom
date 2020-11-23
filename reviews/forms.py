from django import forms
from .models import Review, BioPicture, BioParagraph



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
