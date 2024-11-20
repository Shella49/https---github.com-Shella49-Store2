# 2. Базовый класс User и производные классы для различных типов пользователей

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_details(self):
        return f"Пользователь: {self.username}, Email: {self.email}"

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, address):
        super().__init__(username, email)
        self.address = address

    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}"
