from django.conf.urls import include, url
from django.contrib import admin

from books.views import list_books, create_books

urlpatterns = [
    # Examples:
    # url(r'^$', 'app_library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', list_books, name='index'),
    url(r'^new/$', create_books, name='add_books'),

    # url(r'^comments/$', comments, name='comments'),

    url(r'^admin/', include(admin.site.urls)),

    # url for page login
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='auth_login'),
    # url for page logout
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='auth_logout_next'),
]


# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.HomePageView.as_view(), name='article_list'),
#     # url(r'^ajax_view/$', views.ajax_view, name='ajax_view'),
#     # url(r'^(?P<pk>\d+)/$',
#     #     views.PostDetailView.as_view(), name='article_detail'),
# ]
