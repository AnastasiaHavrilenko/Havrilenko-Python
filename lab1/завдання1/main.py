a = int(input("Введіть а (a > 0): "))
while (a <= 0):
  a = int(input("Число повинно бути додатним. Ведіть а: "))
b = int(input("Введіть b (b > 0): "))
while (b <= 0):
  b = int(input("Число повинно бути додатним. Ведіть b: "))
if a < b:
   x = a / b + 5
elif a == b:
  x = -5
else:
  x = a * a - b
print("Результат обчислення виразу: ", x)
