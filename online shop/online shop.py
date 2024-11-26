
users = {}
products = [
    {"id": 1, "name": "Товар 1", "description": "Описание товара 1", "price": 100},
    {"id": 2, "name": "Товар 2", "description": "Описание товара 2", "price": 150},
    {"id": 3, "name": "Товар 3", "description": "Описание товара 3", "price": 200},]

user_basket = {}
user_orders = {}

class EmailError(Exception):
    def __init__(self, msg):
        self.msg = msg

def valid_email(email):
    if "@" not in email:
        raise EmailError("@ не содержится в email")
    if not email.endswith(".com"):
        raise EmailError("Должен быть домен .com")
    return email


def register_user(name, email, password):
    try:
        valid_email(email)
    except EmailError as e:
        return str(e)

    if email in users:
        return "Пользователь с таким email уже зарегистрирован"

    users[email] = {"name": name,
                    "password": password}
    return "Регистрация прошла успешно"


def login_user(email, password):
    if email in users:
        if users[email]['password'] == password:
            return f"Авторизация прошла успешно. Добро пожаловать, {users[email]['name']}"
        else:
            return "Неверные учетные данные"
    else:
        return "Пользователь не найден"


def get_products():
    return products

def add_to_basket (email, product_id):
    if email not in users:
        return "Пользователь не найден"
    if email not in user_basket :
        user_basket [email] = []

    product = next((i for i in products if i['id'] == product_id))
    if product:
        user_basket [email].append(product)
        return f"Товар {product['name']} добавлен в корзину."
    else:
        return "Товар не найден"


def order(email, delivery_address, payment_method):
    if email not in users:
        return "Пользователь не найден"
    if email not in user_basket  or not user_basket [email]:
        return "Корзина пуста"

    order_items = user_basket [email]
    total_price = sum(item['price'] for item in order_items)
    order_id = len(user_orders) + 1
    user_orders[order_id] = {"email": email,
                             "items": order_items,
                             "total_price": total_price,
                             "delivery_address": delivery_address,
                             "payment_method": payment_method}

    user_basket [email] = []
    return f"Заказ оформлен. ID заказа: {order_id}, Сумма к оплате: {total_price} рублей."



def order_history(email):
    if email not in users:
        return "Пользователь не найден"

    user_order_history = {id: details for id, details in user_orders.items() if details["email"] == email}
    if not user_order_history:
        return "История заказов пуста."
    return user_order_history




name = input("Введите ваше имя: ")
email = input("Введите ваш email: ")
password = input("Введите ваш пароль: ")

print(register_user(name, email, password))


email_login = input("Введите ваш email для авторизации: ")
password_login = input("Введите ваш пароль: ")
print(login_user(email_login, password_login))


print("Список товаров:")



product_ids = input("Введите ID товара для добавления в корзину: ")


delivery_address = input("Введите адрес доставки: ")
payment_method = input("Введите способ оплаты: ")
print(order(email, delivery_address, payment_method))


print("История заказов:")
print(order_history(email))
