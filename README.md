# DisposableMail

`disposablemail-api` — это простая библиотека на Python для работы с сервисом временных почт [DisposableMail](https://www.disposablemail.com/).

## Установка

Вы можете установить библиотеку с помощью pip:

```bash
$ pip install git+https://github.com/cardisnotvalid/disposablemail-api
```

## Использование

### Инициализация

Чтобы начать работу с библиотекой, создайте экземпляр класса `DisposableMail` и используйте его методы для взаимодействия с API.

```python
from disposablemail import DisposableMail

with DisposableMail() as mail_client:
    # Получение временного email
    email = mail_client.get_email()
    print(f"Ваш временный email: {email.address}")
```

### Получение списка сообщений и  сообщения

Метод `get_mailbox` возвращает список сообщений, доступных для временного email. Метод `get_message` возвращает полный текст сообщения по его ID.

```python
from disposablemail import DisposableMail

with DisposableMail() as mail_client:
    # Получение временного email
    email = mail_client.get_email()
    print(f"Ваш временный email: {email.address}")

    # Получение списка сообщений
    mailbox = mail_client.get_mailbox()
    for message in mailbox:
        print(f"Сообщение от: {message.from_}, Тема: {message.subject}")

    # Получение полного текста сообщения
    if mailbox:
        message_id = mailbox[0].id
        message_text = mail_client.get_message(message_id)
        print(f"Текст сообщения: {message_text}")
```

### Ожидание нового сообщения

Метод `wait_message` используется для ожидания нового сообщения с заданным количеством попыток и задержкой между попытками.

```python
from disposablemail import DisposableMail

with DisposableMail() as mail_client:
    # Ожидание нового сообщения
    new_message = mail_client.wait_message(attempts=10, delay=3)
    if new_message:
        print(f"Новое сообщение от: {new_message.from_}, Тема: {new_message.subject}")
    else:
        print("Новое сообщение не получено.")
```

## Лицензия

Этот проект лицензируется в соответствии с условиями [LICENSE](LICENSE).
