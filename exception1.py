"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    quest_and_answ = {"как дела?": "Хорошо!", "что делаешь?": "Программирую"}
    try:                                          
        print("Добро пожаловать в гости к Чат-Боту3000 \nЖду Ваших вопросов")
        while True:
            user_ask = input("user: ")
            if user_ask.lower() == "пока":
                print("До скорого.")
                break
            elif user_ask.lower() in quest_and_answ:
                print(f"Чат-Бот3000: {quest_and_answ[user_ask]}")
            elif user_ask.lower() not in quest_and_answ.keys():
                print("У меня не ответа на твой вопрос.")
    except KeyboardInterrupt:
        print("\nЧат-Бот3000: Пока!")

    
if __name__ == "__main__":
    ask_user()
