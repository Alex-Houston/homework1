"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string_one, string_two):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    if string_one == "" or string_two == "" or not isinstance(string_one, str) or not isinstance(string_two, str):
        return 0
    elif string_one == string_two:
        return 1
    if string_two == "learn":                         #Можно ли сделать это и следующие условия 
        if len(string_one) > len(string_two):         #более компактно и/или красиво?
            return 2, 3
        return 3
    elif len(string_one) > len(string_two):
        return 2
    

    
    
    
if __name__ == "__main__":
    print(main("1", ""))
    print(main("1", "1"))
    print(main("123", "12"))    
    print(main("123", "learn"))
    print(main("1233123123", "learn"))    

    

