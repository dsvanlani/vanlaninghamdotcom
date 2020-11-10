from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('reviews/<str:id>', views.reviewPage, name="reviewPage"),
    path('addReview/', views.addReview, name="addReview"),
    path('post-comment/', views.postComment),
    path('allReviews', views.allReviews, name='allReviews')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)