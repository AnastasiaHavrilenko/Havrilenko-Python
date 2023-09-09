f1 = 0
f2 = 1
print ("Перші 8 чисел з ряду Фібоначчі: ")
print (f1, f2, end = ' ')
sum = f1 + f2
for i in range(2, 8):
  f1, f2 = f2, f1 + f2 
  print (f2, end = ' ')
  sum = sum + f2
print ("\nЇх сума: ", sum)
