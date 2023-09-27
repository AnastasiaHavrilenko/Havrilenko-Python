x = int(input("Введіть кількість елементів масива х = "))

print(f"Введіть {x} елементів масиву:")

arr = [int(input()) for i in range(x)]
sum = 0
kilkist = 0
for t in arr:
  if t < 0:
    sum += t
    kilkist += 1
if kilkist == 0:
  print("В масиві немає від'ємних чисел")
else:
  result = sum / kilkist
  print("Середнє арифметичне від'ємних чисел:", result)
