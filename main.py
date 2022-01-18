from faker import Faker
from .catalog.models import Author, Book, BookInstance

a = Faker()
for i in range(100):
author = Author(first_name=a.first_name(), last_name=a.last_name(), date_of_birth=a.date(), date_of_death=a.date())

