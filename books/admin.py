from django.contrib import admin


from .models import Book, Genre


# Register your models here.
class AboutBook(admin.ModelAdmin):
    list_display = ['author', 'name', 'is_no_draft']
    fieldsets = [
        ('Name author', {'fields': ['author']}),
        ('Information about book', {'fields': ['name','public_date','image', 'description', 'genresbooks']}),
        ('Book is draft', {'fields': ['is_no_draft']})
    ]

    search_fields = ['author']

admin.site.register(Genre)
admin.site.register(Book, AboutBook)
