def find_sequence(user_list, sequence):
    found_indices = []
    for i in range(len(user_list)):
        if user_list[i:i + len(sequence)] == sequence:
            found_indices.append(i)

    if found_indices:
        print(f"Послідовність {sequence} знайдена на індексах: {found_indices}")
    else:
        print(f"Послідовність {sequence} не знайдена в списку.")

# Користувач вводить список
user_input = input("Введіть список елементів через пробіл: ")
user_list = user_input.split()  # Розділити введений рядок на список

# Користувач вводить послідовність для пошуку
sequence_input = input("Введіть послідовність для пошуку через пробіл: ")
sequence = sequence_input.split()  # Розділити введений рядок на список

find_sequence(user_list, sequence)
