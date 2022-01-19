from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^my-books/$', views.LoanedBooksByUserListView.as_view(), name='my-books'),
    re_path(r'^borred-books/$', views.LoanedBooksStaffListView.as_view(), name='borred-books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]