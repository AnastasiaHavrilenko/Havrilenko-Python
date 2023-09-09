x = int(input("Введіть число від 1 до 9: "))
while x < 1 or x > 9:
  x = int(input("Введіть число від 1 до 9: "))
for i in range (1,x + 1):
    for j in range (1,i + 1):
      print (j, end = ' ')
    print (" ")
