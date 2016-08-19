from django.contrib import admin


from .models import Book, Genre


# Register your models here.
class AboutBook(admin.ModelAdmin):
    fieldsets = [
        ('Name author', {'fields': ['author']}),
        ('Information about book', {'fields': ['name', 'image', 'description', 'genresbooks']}),
        # ('Information about book', {'fields': ['name', 'date_publication','image', 'description', 'genresbooks']}),

        ('Book is draft', {'fields': ['is_draft']})
    ]
    list_filter = ['author']
    list_display = ('is_draft',)

admin.site.register(Genre)
admin.site.register(Book, AboutBook)
