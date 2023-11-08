try:
  # Створення текстового файлу TF4_1
  with open("TF4_1.txt", "w") as file:
      file.write("Це є рядок\n")
      file.write("Це є рядок із декількома словами\n")
      file.write("А це, можливо, третій рядок\n")

  # Читання вмісту файла TF4_1 та підрахунок кількості слів з різною довжиною
  word_lengths = {}
  with open("TF4_1.txt", "r") as file:
      for line in file:
          words = line.split()
          for word in words:
              word_length = len(word)
              if word_length in word_lengths:
                  word_lengths[word_length] += 1
              else:
                  word_lengths[word_length] = 1

  # Запис результату у файл TF4_2
  with open("TF4_2.txt", "w") as file:
      for length, count in word_lengths.items():
          file.write(f"Слово із {length} символів: {count} шт.\n")

  # c) Читання вмісту файла TF4_2 та друк результату
  with open("TF4_2.txt", "r") as file:
      for line in file:
          print(line, end="")

except FileNotFoundError:
  print("Помилка: файл не знайдено.")
except Exception as e:
  print(f"Помилка: {e}")
