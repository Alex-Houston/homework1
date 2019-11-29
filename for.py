"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    lst = [
        {'school_class': '9А', 'scores': [3,4,4,5,2]},
        {'school_class': '9Б', 'scores': [4,3,5,4,1]},
        {'school_class': '9В', 'scores': [3,5,4,5,5]}
    ]
    all_scores = 0
    all_students = 0
    for class_counter in lst:
        class_scores = 0
        for scores_counter in class_counter['scores']:
            class_scores += scores_counter
        print(f"Средний балл в {class_counter['school_class']}: ", class_scores/len(class_counter['scores']))
        all_scores += class_scores
        all_students += len(class_counter['scores'])
    print(f"Средний балл всех учеников: {all_scores/all_students}")
    
    
if __name__ == "__main__":
    main()
