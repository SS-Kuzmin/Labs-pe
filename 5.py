class MailServer:
    def __init__(self):
        # Инициализация почтового ящика
        self.mailbox = []

    def receive_mail(self):
        # Метод для получения письма из ящика
        if self.mailbox:
            return self.mailbox.pop(0)  # Возвращаем первое письмо из списка и удаляем его из ящика
        else:
            return None

    def store_mail(self, mail):
        # Метод для хранения письма в ящике
        self.mailbox.append(mail)


class Mail:
    def __init__(self, sender, recipient, message):
        # Инициализация атрибутов письма: отправитель, получатель, текст сообщения
        self.sender = sender
        self.recipient = recipient
        self.message = message


class MailClient:
    def __init__(self, server, user):
        # Инициализация клиента с указанием сервера и пользователя
        self.server = server
        self.user = user

    def receive_mail(self):
        # Метод для получения письма
        return self.server.receive_mail()

    def send_mail(self, server, recipient, message):
        # Метод для отправки письма
        if server in available_servers:
            # Проверка доступности сервера
            mail = Mail(self.user, recipient, message)  # Создание объекта письма
            server.store_mail(mail)  # Сохранение письма на сервере
            print(f"Mail sent to {recipient} on {server}")  # Вывод сообщения об успешной отправке
        else:
            print("Error: Server not available")  # Вывод сообщения об ошибке

    def connect_to_server(self, server):
        # Метод для подключения к другому серверу
        self.server = server


# Создадим список доступных серверов
available_servers = []

# Пример использования
server1 = MailServer()
server2 = MailServer()
available_servers.extend([server1, server2])  # Добавление серверов в список доступных

client = MailClient(server1, "user1")  # Создание клиента
client.send_mail(server1, "user2", "Hello, User2!")  # Отправка письма с сервера 1 на сервер 1
client.send_mail(server2, "user3", "Hello, User3!")  # Отправка письма с сервера 1 на сервер 2
print(client.receive_mail())  # Получение письма с сервера 1
client.connect_to_server(server2)  # Подключение к серверу 2
print(client.receive_mail())  # Получение письма с сервера 2
