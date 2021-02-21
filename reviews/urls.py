from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('', views.home, name="home"),
    path('reviews/<str:id>', views.reviewPage, name="reviewPage"),
    path('addReview/', views.addReview, name="addReview"),
    path('post-comment/', views.postComment),
    path('allReviews', views.allReviews, name='allReviews'),
    path('editBio', views.editBio, name='editBio'),
    path('editBio/changePicture', views.changePicture, name="changePicture"),
    path('editBio/changeBioParagraph', views.changeBioParagraph, name="changeBioParagraph"),
    path('favicon.png', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.png'))),
    path('articles', views.articlesPage, name="articlesPage"),
    path('articles/<str:id>', views.articlePage, name="articlePage"),
    path('addArticle', views.addArticle, name="addArticle")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)