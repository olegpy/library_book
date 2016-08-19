from django.conf.urls import include, url
from django.contrib import admin

from .views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'app_library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),

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
