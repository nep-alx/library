from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include

from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/file/all$', views.FileList.as_view()),
    url('^api/file/(?P<book>\d+)$', views.BookFiles.as_view()),
    url('^api/loan/(?P<book>\d+)$', views.BookLoans.as_view()),
    url('^api/loan/add$', views.LoanAdd.as_view()),
    url('^api/book/search$', views.BookSearch.as_view()),
    url('^accounts/', include('django.contrib.auth.urls'))
]
