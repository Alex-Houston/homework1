"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_say = input("Как дела?\n")
        if user_say.lower() == "хорошо":
            print("Вот и славно.")
            break


    
if __name__ == "__main__":
    ask_user()
