import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def my_function(x):
    return 2**x * np.sin(10*x)

# Генерація значень x в заданому діапазоні
x_values = np.linspace(-3, 3, 1000)

# Обчислення відповідних значень y
y_values = my_function(x_values)

# Налаштування вигляду графіка
plt.plot(x_values, y_values, linestyle='-', color='blue', linewidth=2, label=r'$Y(x) = 2^x \sin(10x)$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Графік функції')
plt.xlabel('x')
plt.ylabel('Y(x)')

# Виведення легенди
plt.legend()

# Показати графік
plt.show()Л
