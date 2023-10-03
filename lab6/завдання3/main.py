def count(text):
    golosni = "aeiouy"
    text = text.lower()  # Переводимо весь текст до нижнього регістру

    golosni_count = 0
    prugolosni_count = 0

    for char in text:
        if char.isalpha():  # Перевіряємо, чи символ є літерою.
            if char in golosni:
                golosni_count += 1
            else:
                prugolosni_count += 1

    return golosni_count, prugolosni_count

# Введення тексту користувачем
input_text = input("Введіть текст: ")
golosni, prugolosni = count(input_text)

print(f"Голосних літер: {golosni}")
print(f"Приголосних літер: {prugolosni}")

if golosni > prugolosni:
    print("Голосних літер більше в цьому тексті.")
elif prugolosni > golosni:
    print("Приголосних літер більше в цьому тексті.")
else:
    print("Кількість голосних та приголосних літер однакова в цьому тексті.")
