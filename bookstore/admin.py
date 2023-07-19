from django.contrib import admin
from .models import Books, Authors
# Register your models here.
@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):

    pass

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):

    pass
