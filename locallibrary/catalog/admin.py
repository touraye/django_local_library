from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


class BookInline(admin.TabularInline):
    model = Book
    
# admin.site.register(Author)
# Register the Admin classes for Author using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
    inlines = [BookInline]
    
# admin.site.register(Book)   
# Register the Admin classes for Book using the decorator
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    
@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    
    inlines = [BookInstanceInline]


# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)

