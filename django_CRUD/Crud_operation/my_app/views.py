from django.shortcuts import render, redirect
from .models import Book

def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publication_date = request.POST['publication_date']
        Book.objects.create(title=title, author=author, publication_date=publication_date)
        return redirect('book_list')
    return render(request, 'my_app/create_book.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'my_app/book_list.html', {'books': books})

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_date = request.POST['publication_date']
        book.save()
        return redirect('book_list')
    return render(request, 'my_app/update_book.html', {'book': book})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'my_app/delete_book.html', {'book': book})

