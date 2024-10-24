from importlib.resources import contents
from xmlrpc.client import boolean


def send_email ( message, recipient, *,sender = "university.help@gmail.com"):
    string_ = [ '.com', '.ru', '.net']
    string_1 = '@'
    boolen = False
    for i in range (len(string_)):
        if sender.endswith(string_[i]) == True:
            boolen = True
    boolen_1 = string_1 in sender
    boolen_2 = sender == recipient
    boolen_3 = "university.help@gmail.com" in sender
    if boolen == False or boolen_1 == False:
        print (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif boolen_2 == True:
        print ("Нельзя отправить письмо самому себе!")
    elif boolen_3 == True:
        print (f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else: print ( f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')