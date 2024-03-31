from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import F
from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import *
from .models import *

def index(request):
    return render(request, "main.html",)

def books(request):
    genre = Genre.objects.all()
    lang = Language.objects.all()
    print = Print.objects.all()
    books = Book.objects.all()
    if request.method=='POST':
        if request.POST.get("book")!='':
            books = books.filter(name__icontains=str(request.POST.get("book")))
        if request.POST.get("genre")!='':
            books = books.filter(genre__name=request.POST.get("genre"))
        if request.POST.get("lang")!='':
            books = books.filter(lang__name=request.POST.get("lang"))
        if request.POST.get("print")!='':
            books = books.filter(print__name=request.POST.get("print"))
        if request.POST.get("author")!='':
            books = books.filter(authors__fio__icontains=request.POST.get("author"))
    return render(request, "books.html",
                  {'title':'Книги','books':books,'genre':genre,'lang':lang,'print':print})

def this_book(request,book_id):
    thisbook=Book.objects.get(pk=book_id)
    count_like = thisbook.profile_set.count()
    return render(request, "thisbook.html",{'thisbook':thisbook,'count_like':count_like})

def authors(request):
    if request.method == "POST":
        need_author = request.POST.get("author")
        all_authors = Author.objects.all()
        authors = list()
        for a in all_authors:
            if need_author in a.fio:
                authors.append(a)
    else:
        authors = Author.objects.all()
    return render(request,"authors.html",{'title':'Авторы','authors':authors})

def this_author(request,author_id):
    thisauthor = Author.objects.get(pk=author_id)
    hisbooks = thisauthor.book_set.all() #получение всех книг связанных с автором
    return render(request, "thisauthor.html", {'thisauthor': thisauthor,'hisbooks':hisbooks})

@permission_required(perm='ReadTheCity.add_book', raise_exception=True)#будет страница ошибки
def addbook(request):
    if request.method=='POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddBookForm()
    return render(request, "addbook.html", {'title':'Добавление книги','form': form})

def login_user(request):
    if request.method=='POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                form.add_error(None, 'Неверно введен логин или пароль')
                return render(request, 'registration/login.html', {'title':'Вход','form':form})
    else:
        form = LoginUserForm()
    return render(request, 'registration/login.html',{'title':'Вход','form':form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method=='POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)#запись в БД пока не заносится
            user.set_password(form.cleaned_data['password'])#шифровка пароля
            user.save()#занесение в БД
            Profile.objects.create(user=user)
            return render(request,'registration/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html',{'form':form,'title':'Регистрация'})

@login_required
def profile_view(request):
    profile = Profile.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile,
                 initial={'birth': profile.birth})
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html',
      {'user_form': user_form, 'profile_form': profile_form,'profile':profile,'title':'Профиль'})

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_change_done')#запускается только при надобности

def counter(request):
    book_id = request.GET.get('book_id')
    Book.objects.filter(id=book_id).update(upload = F('upload')+1)
    return HttpResponseRedirect(reverse('this_book', args=[book_id]))

def like_page(request):
    books = Profile.objects.get(user__username=request.user.username).books.all()
    return render(request, 'likepage.html',{'books':books,'title':'Избранное'})

def add_like(request):
    book_id = request.GET.get('book_id')
    book = Book.objects.get(id=book_id)
    profile = Profile.objects.get(user__username=request.user.username)
    book.profile_set.add(profile)
    if request.GET.get('page')=='all':
        return redirect(to='books')
    if request.GET.get('page')=='one':
        return HttpResponseRedirect(reverse('this_book', args=[book_id]))


def drop_like(request):
    book_id = request.GET.get('book_id')
    book = Book.objects.get(id=book_id)
    profile = Profile.objects.get(user__username=request.user.username)
    book.profile_set.remove(profile)
    return redirect(to='like_page')







