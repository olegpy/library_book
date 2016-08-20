# from django.views.generic.base import TemplateView
# from django.http import HttpResponse
# from django.views.generic.detail import DetailView
# from django.views.decorators.csrf import csrf_exempt
# import json
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

from .models import Book
from .forms import BookModelForm
from django.utils.timezone import now

# class HomePageView(TemplateView):
#     template_name = "books/book_list.html"

#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         context['page_title'] = "Article list"
#         return context


def list_books(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=8)
    books = Book.objects.filter(public_date__range=(startdate, enddate))
    return render(request, 'books/book_list.html', {'books': books})

def create_books(request):
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES)
        # for filename, file in request.FILES.iteritems():
        #     print 'ss'
        #     name = request.FILES[filename].name
        #     print name
        # self.object = form.save(commit=False)
        # self.object.author = self.request.user
        # self.object.published_date = timezone.now()
        form_temp = form.save(commit=False)
        form_temp.author_post = request.user
        form_temp.save()
        # form_temp.author = request.user
        if form.is_valid():
            book = form.save()
            data = form.cleaned_data
            print 'valid'
            return redirect('index')

    else:
        form = BookModelForm()
    return render(request, 'books/add.html', {'form': form})

         # def list_view(request):
#     reguest_course = request.GET
#     if 'course_id' in reguest_course:
#         list_students = Student.objects.filter(
#             courses=reguest_course['course_id'])
#     else:
#         list_students = Student.objects.all()
# return render(request, 'students/list.html', {'list_students': list_students})


# @csrf_exempt
# def ajax_view(request):
#     end = 5
#     if request.method == 'POST' and request.is_ajax():
#         end = request.POST.get('count', 0)
#         return ajax_response(end)

#     if request.method == 'GET' and request.is_ajax():
#         return ajax_response(end)


# def ajax_response(end):
#     articles = Article.objects.filter(
#         is_published=True).values('title', 'image', 'text', 'pk')[:end]
#     return HttpResponse(json.dumps(list(articles)),
#                         content_type='application/json')


# class PostDetailView(DetailView):
#     model = Article
#     template_name = 'articles/article_detail.html'
#     context_object_name = 'article'

#     def get_context_data(self, **kwargs):
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         print context
#         context['page_title'] = "Article detail"
#         return context
