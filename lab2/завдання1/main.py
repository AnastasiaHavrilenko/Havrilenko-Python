def function (m):  #Функція, що знаходить число
  z = 1 / (m+2)**0.5
  return z
def shlyah (n):   #Функція, що обчислює шлях спортсмена на тренуваннях
  if n == 1 :
    result = 10
  else:
    result = 10
    probig = 10
    for i in range (1,n,1):
      probig *=  1.16
      result += probig
  return result
m = int(input("Введіть значення m ( m >= 0): "))
while m < 0:
  m = int(input("Неправильне значеня. Введіть значення m ( m >= 0): "))
print ("Значення виразу z = ", function(m))
n = int(input("Введіть кількість днів тренування спортсмена: "))
while n < 0:
  n = int(input("Неправильне значеня. Введіть значення n > 0: "))
print ("Сумарний шлях, який пробіжить спортсмен за дні тренування: ", shlyah(n))