from django.contrib import admin
from .models import Genre,Language,Book,Author, BookInstance
# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance)
admin.site.register(Author)

