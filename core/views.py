from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Prestamo

def home(request):
    books = Book.objects.all()
    return render(request, 'core/home.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

@login_required
def mis_prestamos(request):
    prestamos = Prestamo.objects.filter(user=request.user)
    return render(request, 'core/prestamos.html', {'prestamos': prestamos})

@login_required
def rentar_libro(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.available:
        Prestamo.objects.create(user=request.user, book=book)
        book.available = False
        book.save()
    return redirect('home')
