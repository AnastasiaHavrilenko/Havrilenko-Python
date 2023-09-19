def slova_n(rechennya):
    slova = rechennya.split()  # Розбиваємо речення на слова
    litera_n = []

    for s in slova:
        if s.startswith('н') or s.startswith('Н'):  # Перевіряємо на початкову літеру 'н' або 'Н'
            litera_n.append(s)

    return len(litera_n)

rechennya = input("Введіть речення: ")
result = slova_n(rechennya) 

print("Кількість слів, що починаються з 'н':", result)
