def add_element():

    A = list(map(int,input('Введіть список елементів: ').split())) # Розділити введений рядок на список

    print(A)

    position = int(input("Введіть позицію для вставки: "))
    while position < 0 or position > len(A):
       print("Помилка: неправильна позиція")
       position = int(input("Введіть позицію для вставки: "))    
    element = int(input("Введіть елемент для вставки: "))
    A.insert(position, element)
    print(A)
  
add_element()
