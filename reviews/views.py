from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from .forms import AddReviewForm, ChangeBioPictureForm, ChangeBioParagraphForm, AddArticleForm


# Custom Functions

def getBio():

    bioPicture = BioPicture.objects.order_by('-id').first()
    bioParagraph = BioParagraph.objects.order_by('-id').first()

    bio = {
        "bioPicture": bioPicture,
        "bioParagraph": bioParagraph
    }

    return bio
# Takes in a string as a parameter and looks
# for matching results in the Author and Title columns


def getSearchResults(string):
    reviews = Review.objects.filter(bookTitle__icontains=string)
    reviews |= Review.objects.filter(bookAuthor__icontains=string)
    return reviews


# Review Relevant Views
def home(request):
    recentReviews = Review.objects.all().order_by('-id')[:6]
    allReviews = Review.objects.all().order_by('bookAuthorLastName')

    context = {
        "recentReviews": recentReviews,
        "allReviews": allReviews,
        "bio": getBio(),
    }
    return render(request, 'reviews/home.html', context)


def reviewPage(request, id):
    review = Review.objects.get(id=id)
    comments = Comment.objects.all().filter(parentReview=Review.objects.get(id=id)).order_by('-timestamp')

    context = {
        "review": review,
        "comments": comments
    }

    return render(request, 'reviews/reviewPage.html', context)


@login_required
def addReview(request):
    if request.method == "POST":
        form = AddReviewForm(request.POST, request.FILES)  # Gets the form data
        if form.is_valid():
            form.save()
            message = "Successfully created article."
            error = ""
        else:
            message = ""
            error = "Unable to create article"
    
    else:
        message = ""
        error = ""
    
    context = {
        "error": error,
        "message": message,
        "form": AddReviewForm(),
    }

    return render(request, "reviews/addReview.html", context)

@login_required
def addArticle(request):
    if request.method == "POST":
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Successfully created article."
            error = ""
        else:
            message = ""
            error = "Unable to create article"
    
    else:
        message = ""
        error = ""
    
    context = {
        "error": error,
        "message": message,
        "form": AddArticleForm(),
    }
    
    return render(request, "articles/addArticle.html", context)


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
                parentReview=Review.objects.get(id=comment['parentReview'])
            )
            newComment.save()
            return JsonResponse({"message": "success"})
        except Exception as e:
            return JsonResponse({"message": e.__str__()})


def allReviews(request):
    try:
        reviews = getSearchResults(request.GET['search']).order_by('bookAuthorLastName')
        search = request.GET['search']
        context = {
            "reviews": reviews,
            "search": search,
        }
    except KeyError:
        reviews = Review.objects.all().order_by('bookAuthorLastName')
        context = {"reviews": reviews}

    return render(request, 'reviews/allReviews.html', context)

def articlesPage(request):
 
    articles = Article.objects.all().order_by('articleTitle')
    context = {"articles": articles}

    return render(request, 'articles/articlesPage.html', context)

def articlePage(request, id):
    try:
        article = Article.objects.get(id=id)
    except:
        return redirect('home')

    context = { "article": article }
    return render(request, 'articles/articlePage.html', context)

@login_required
def editBio(request):
    pictureForm = ChangeBioPictureForm()
    paragraphForm = ChangeBioParagraphForm()
    context = {
        "bio": getBio(),
        "pictureForm": pictureForm,
        "paragraphForm": paragraphForm,
    }

    return render(request, 'reviews/editBio.html', context)

@login_required
def changePicture(request):
    if request.method == "POST":
        form = ChangeBioPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return redirect('editBio')

def changeBioParagraph(request):
    if request.method == "POST":
        form = ChangeBioParagraphForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('editBio')