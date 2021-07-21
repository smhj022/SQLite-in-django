from django.contrib import admin

from .models import Author, Book, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)

admin.site.register(Author)

admin.site.register(Address)

admin.site.register(Country)