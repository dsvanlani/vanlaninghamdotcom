from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from .forms import AddReviewForm


# Custom Functions

# Takes in a string as a parameter and looks
# for matching results in the Author and Title columns


def getSearchResults(string):
    reviews = Review.objects.filter(bookTitle__icontains=string)
    reviews |= Review.objects.filter(bookAuthor__icontains=string)
    return reviews


# Views


def home(request):
    reviews = Review.objects.all().order_by('-id')[:6]

    context = {
        "reviews": reviews
    }
    return render(request, 'reviews/home.html', context)


def reviewPage(request, bookISBN):
    review = Review.objects.get(bookISBN=bookISBN)
    comments = Comment.objects.all().filter(parentReview=Review.objects.get(bookISBN=bookISBN)).order_by('-timestamp')

    # Read the file
    f = review.content
    content = f.read()
    f.close()

    context = {
        "review": review,
        "content": content,
        "comments": comments
    }

    return render(request, 'reviews/reviewPage.html', context)


@login_required
def addReview(request):
    # TODO make this handle docx files
    if request.method == "POST":
        form = AddReviewForm(request.POST, request.FILES)  # Gets the form data
        if form.is_valid():
            form.save()
            message = "success"
        else:
            message = "failed"
    else:
        message = ""

    context = {
        "message": message,
        "form": AddReviewForm(),
    }

    return render(request, "reviews/addReview.html", context)


@csrf_exempt
def postComment(request):
    if request.method != "POST":
        raise Http404("Page Not Found")
    else:
        try:
            data = json.loads(request.body)
            comment = data['comment']
            newComment = Comment(
                commenterName=comment['commenterName'],
                commenterEmail=comment['commenterEmail'],
                commentBody=comment['commentBody'],
                parentReview=Review.objects.get(bookISBN=comment['parentReview'])
            )
            newComment.save()
            return JsonResponse({"message": "success"})
        except Exception as e:
            return JsonResponse({"message": e.__str__()})


def allReviews(request):
    try:
        reviews = getSearchResults(request.GET['search'])
        search = request.GET['search']
        context = {
            "reviews": reviews,
            "search": search,
        }
    except KeyError:
        reviews = Review.objects.all()
        context = {"reviews": reviews}

    return render(request, 'reviews/allReviews.html', context)
