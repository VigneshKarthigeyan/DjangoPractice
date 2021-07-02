from book_outlet.models import Address, Book,Author, Country
from django.contrib import admin

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":('title',)}
    list_display=("title","author","rating")
    list_filter=("author",)

admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)