from django.contrib import admin
from .models import Category, Book, Prestamo

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'available')
    list_filter = ('available', 'category')
    search_fields = ('title', 'author')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'fecha_prestamo', 'devuelto')
    list_filter = ('devuelto',)
