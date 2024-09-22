def send_email(message, recipient, sender="university.help@gmail.com"):
    spisok_ = ['.com','.ru','.net']
    n = 0
# Проверяем есть ли символ @
    if '@' not in sender and recipient:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)

# Проверяем есть ли окончание .ru .com .net
    for i in spisok_:
        if  i not in sender and recipient: #Проверка на корректность e-mail отправителя и получателя.
            n = n + 1
        if n == 3:
            return print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)

# Проверяем отправитель равен ли получателю
    if sender == recipient:
        return print("Нельзя отправить письмо самому себе!")

# Проверяем на отправителя не по умолчанию и отправялем в противном случае
    if sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('Письмо успешно отправлено с адреса', sender, ' на адрес ', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')