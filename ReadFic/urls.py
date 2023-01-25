
from django.contrib import admin
from django.urls import path, include
from books import views as books_views
from user_auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books', books_views.BookAllView.as_view()),
    path('api/user/books', books_views.BookMyView.as_view()),
    path('api/auth/login', auth_views.LoginAPIView.as_view()),
    path('api/', books_views.BookRandomView.as_view()),
    path('api/auth/registration/', auth_views.UserView.as_view(), name='index'),
]
