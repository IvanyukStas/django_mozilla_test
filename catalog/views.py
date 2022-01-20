import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import generic

from catalog.forms import RenewBookForm
from catalog.models import Book, BookInstance, Author

@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )


@login_required
@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_inst = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            messages.success(request, 'Успешно обновили дату возврата книги!')
            return HttpResponseRedirect(reverse('borred-books'))

    else:
        proposed_renewal_data = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(initial={'renewal_form': proposed_renewal_data})
    context = {'form': form,
               'book_inst': book_inst
               }
    return render(request, 'catalog/book_renew_librarian.html', context=context)


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin,  generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o')


class LoanedBooksStaffListView(LoginRequiredMixin, generic.ListView):
    # permission_required = 'can_mark_returned'
    model = BookInstance
    paginate_by = 10
    template_name = 'catalog/bookinstacne_list_for_staff.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').filter(borrower__isnull=False).order_by('due_back')


class AuthorCreate(generic.edit.CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '12/10/2016'}


class AuthorUpdate(generic.edit.UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth','date_of_death']


class AuthorDelete(SuccessMessageMixin, generic.edit.DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    success_message = 'Вы удалили автора из базы библиотеки!'


class BookCreate(generic.edit.CreateView):
    model = Book
    fields = '__all__'


class BookInstanceCreate(generic.edit.CreateView):
    model = BookInstance
    fields = '__all__'
    initial = {'due_back': '22/01/2022'}
    success_url = reverse_lazy('books')




class BookInstanceUpdate(generic.edit.UpdateView):
    model = BookInstance
    fields = ['book', 'imprint', 'due_back', 'borrower', 'status', ]

    def gen_success_url(self):
        print(self.object.book.id)
        return reverse_lazy('book-detail', kwargs={'pk': self.object.book.id})

class BookInstanceDelete(SuccessMessageMixin , generic.edit.DeleteView):
    model = BookInstance
    success_url = reverse_lazy('books')
    success_message = 'Вы удалили книгу!'