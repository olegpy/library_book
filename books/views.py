from django.shortcuts import render, redirect
from datetime import datetime, timedelta

from .models import Book
from .forms import BookModelForm


def list_books(request):
    all_books = Book.objects.all()
    if request.user.is_authenticated():
        books = all_books.filter(is_no_draft=True)
    else:
        enddate = datetime.today()
        startdate = enddate - timedelta(days=8)
        books = all_books.filter(public_date__range=(startdate, enddate), is_no_draft=True)
    return render(request, 'books/book_list.html', {'books': books})


def author_books(request):
    books = Book.objects.filter(author_post=request.user)
    return render(request, 'books/author_books.html', {'books': books})

def create_books(request):
    if request.POST:
        form = BookModelForm(request.POST)
        form_temp = form.save(commit=False)
        form_temp.author_post = request.user
        form_temp.save()
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookModelForm()
        print form
        # form = BookModelForm()
    return render(request, 'books/add.html', {'form': form})
