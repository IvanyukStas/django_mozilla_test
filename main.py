# import random
#
# from faker import Faker
# from catalog.models import Author, Book, BookInstance, Language
#
# a = Faker()
# language = Language.objects.all()
# genre = ['fantasy', 'mystic', 'story']
# author = Author(genre=random.choice(genre), first_name=a.first_name(), last_name=a.last_name(), date_of_birth=a.date(), date_of_death=a.date())
# author.save()
# author = Author.objects.all()
#
# book = Book(title=a.word(), summary=a.text(), isbn=random.randrange(10000000000, 9999999999999), author=random.choice(author), language=random.choice(language), )
# book.save()
# books = Book.objects.all()
# l_status = ['m', 'o', 'a', 'r']
# inst = BookInstance(book=random.choice(books), status=random.choice(l_status))
# inst.save()

a = [1, 2]
yield(a)