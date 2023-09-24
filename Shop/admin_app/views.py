from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book
from .cart import Cart
from .forms import OrderForm


def home(request):
    # Отримання списку всіх книг з бази даних
    books = Book.objects.all()
    # Код для обробки запиту для головної сторінки
    return render(request, 'admin_app/home.html', {'books': books})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматично автентифікуємо користувача після реєстрації
            login(request, user)
            return redirect('home')  # Замініть 'home' на URL вашої головної сторінки
    else:
        form = UserCreationForm()
    return render(request, 'admin_app/register.html', {'form': form})


def filter_books(request):
    # Отримуємо параметри фільтрації з GET-запиту
    category = request.GET.get('category')
    author = request.GET.get('author')

    # Відбираємо книги за параметрами фільтрації
    books = Book.objects.all()
    if category:
        books = books.filter(category=category)
    if author:
        books = books.filter(author=author)

    return render(request, 'admin_app/book_list.html', {'books': books})


def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    cart = Cart(request)
    cart.add(book=book)
    return redirect('cart')


def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        # Якщо користувач відправляє форму замовлення
        form = OrderForm(request.POST)
        if form.is_valid():
            # Створюємо замовлення
            order = form.save()
            cart.clear()  # Очищаємо корзину після оформлення замовлення
            return render(request, 'admin_app/order_success.html', {'order': order})
    else:
        # Якщо це GET-запит, відображаємо форму замовлення
        form = OrderForm()

    return render(request, 'admin_app/checkout.html', {'cart': cart, 'form': form})
