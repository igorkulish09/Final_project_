class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            # Якщо кошик не існує в сесії, створіть порожній кошик
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, book):
        # Додаємо книгу до кошика або збільшуємо кількість, якщо вона вже там є
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 1, 'price': str(book.price)}
        else:
            self.cart[book_id]['quantity'] += 1
        self.save()

    def remove(self, book):
        # Видаляємо книгу з кошика
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def save(self):
        # Зберігаємо кошик в сесії
        self.session['cart'] = self.cart
        self.session.modified = True

    def clear(self):
        # Очищаємо кошик
        del self.session['cart']
        self.session.modified = True
