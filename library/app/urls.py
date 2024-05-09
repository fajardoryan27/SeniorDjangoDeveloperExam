from django.urls import path,include
from django.conf import settings
from . import views
from .views import BookDetails,BookList,AuthorDetails,AuthorList,GenreList,GenreDetails
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # API Token - to have access to products API
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # API Refresh Token
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API Verify Token
    path('tokenverify/', TokenVerifyView.as_view(), name='token_refresh'),

    # API for Products GET and POST
    path('books/', BookList.as_view()),
    # API For PUT,PATCH and Delete
    path('books/<str:pk>', BookDetails.as_view()),

    path('authors/', AuthorList.as_view()),
    # API For PUT,PATCH and Delete
    path('authors/<str:pk>', AuthorDetails.as_view()),

    path('genres/', GenreList.as_view()),
    # API For PUT,PATCH and Delete
    path('genres/<str:pk>', GenreDetails.as_view()),

    # path('book/', book),
    path("create_books", views.createBooks, name="create_books"),
    path("update_books/<str:pk>", views.updateBooks, name="update_books"),
    path("delete_books/<str:pk>", views.deleteBooks, name="delete_books"),
    path("", views.home, name="index"),
    # path("", views.home2, name="home"),
    path("signup/", views.authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
        

]