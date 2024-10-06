def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    if recipient.count('@') == 0 or sender.count('@') == 0:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient.endswith('.ru') != True and recipient.endswith('.com') != True and recipient.endswith('.net') != True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender.endswith('.ru') != True and sender.endswith('.com') != True and sender.endswith('.net') != True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender != "university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
send_email('Проверка связи', 'dasha@mail.net', sender='masha@mail.ru')
send_email('Пожалуйста, проверьте сообщение', 'tutor@gmail.com')
send_email('Высылаю список вакансий', 'alex@mail.ru', sender='job@box.uk')
send_email('Не забудьте об оплате', 'olgagmail.net', sender='masha@mail.ru')
send_email('Напоминание о важном собрании', 'alex@mail.ru', sender='alex@mail.ru')