from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','city','birth')
    list_display_link = ('id','user')
    search_fields = ('user',)
admin.site.register(Profile, ProfileAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','fio')
    list_display_link = ('id','fio')
    search_fields = ('fio',)
admin.site.register(Author,AuthorAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Language,LanguageAdmin)

class PrintAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','city')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Print,PrintAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Genre,GenreAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','isbn')
    list_display_link = ('id', 'name')
    search_fields = ('name','isbn')
admin.site.register(Book,BookAdmin)

