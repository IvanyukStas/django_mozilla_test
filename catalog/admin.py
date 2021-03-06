from django.contrib import admin
from catalog.models import Book, Author, BookInstance, Language, Genre


# Register your models here.
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )
    list_per_page = 50


admin.site.register(Book)
admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)

