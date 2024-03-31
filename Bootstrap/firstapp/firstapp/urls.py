"""
URL configuration for firstapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from ReadTheCity import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('books/',views.books, name='books'),
    path('this_book/<int:book_id>/',views.this_book, name='this_book'),
    path('addbook/',views.addbook,name='addbook'),
    path('authors/',views.authors,name='authors'),
    path('this_author/<int:author_id>/',views.this_author, name='this_author'),
    path('profile/',views.profile_view,name='profile'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register, name='register'),
    path('password_change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(
        template_name='registration/password_changedone.html'), name='password_change_done'),
    path('upload/', views.counter,name='counter'),
    path('like_page/', views.like_page, name='like_page'),
    path('add_like/', views.add_like, name='add_like'),
    path('drop_like/',views.drop_like, name='drop_like')
]

#включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

