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
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librian'),
]
#crud author
urlpatterns += [
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
#crud book

urlpatterns += [
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^bookinstance/create/(?P<pk>\d+)$', views.BookInstanceCreate.as_view(), name='bookinstance_create'),
    re_path(r'^book/(?P<pk>[-\w]+)/update/$', views.BookInstanceUpdate.as_view(), name='bookinstance_update'),
    re_path(r'^book/(?P<pk>\d+)/delete/$', views.BookInstanceDelete.as_view(), name='book_delete'),
]