import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#data = pd.read_excel('Инфа_зачёт.xlsx')
#data.iloc[1:,0]
X = np.array([3.42,3.39,3.36,3.32,3.29,3.26,3.23,3.19,3.16,3.13,3.11,3.08,3.05,3.02,2.99,2.97,2.94,2.92,]) 
Y = np.array([0.06,0.09,0.13,0.17,0.22,0.27,0.32,0.36,0.41,0.48,0.54,0.61,0.67,0.75,0.84,0.93,1.01,1.09,])  
points_X1 = X[1:12:1]
points_Y1 = Y[1:12:1]
points_X2 = X[13:19:1]
points_Y2 = Y[13:19:1]

x_array = [points_X1, points_X2]
y_array = [points_Y1, points_Y2]
m_array = np.zeros(2)
c_array = np.zeros(2)

for i in range(2):
    m_array[i], c_array[i] = np.polyfit(x_array[i], y_array[i], 1)

for i in range(2):
    print(f"Уравнение линий для точек {i+1}")
    print(f" y = {m_array[i]:.2f}x + {c_array[i]:.2f}")
plt.figure(figsize=(12, 8))
plt.errorbar(X, Y, fmt='o', capsize=5)

# Пределы продления
x_full_range = np.linspace(min(X) - 1, max(X) + 1, 100)

# Построение прямых
cnt = 0
for i in range(2):
      cnt += 1
      plt.plot(x_full_range, m_array[i] * x_full_range + c_array[i], label=f'Прямая Y{cnt}', linestyle='-')

# Добавление осей координат
plt.axhline(0, color='black', linewidth=1) # Ось X
plt.axvline(0, color='black', linewidth=1) # Ось Y

# Настройки графика
plt.title('График зависимости lnU+1 от 1000/T')
plt.xlabel('1000/T, 1/мК')
plt.ylabel('lnU+1')
plt.legend()

# Настройка сетки
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)  # Основная сетка с интервалом разбиения
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)  # Дополнительная сетка

# Установка основных и дополнительных делений
plt.minorticks_on()
plt.xticks(np.arange(min(X) - 0.1, max(X) + 0.1, 0.1))
plt.yticks(np.arange(0.1, 1.2, 0.1))
plt.gca().set_xticks(np.arange(min(X) - 0.1, max(X) + 0.1, 0.01), minor=True)
plt.gca().set_yticks(np.arange(0, 1.2, 0.02), minor=True)
plt.xlim([min(X) - 0.1, max(X) + 0.1])
plt.ylim([0, 1.2])
plt.show()
