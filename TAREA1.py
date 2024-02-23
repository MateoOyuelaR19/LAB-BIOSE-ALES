import numpy as np
import matplotlib.pyplot as plt
print("Hola mundo")
a = np.array([3.1, 1, -0.5, -3.2, 6])
b = np.array([1, 3, 2.2, 5.1, 1])
fila1 = [2, -1, -3]
fila2 = [4, 1.5, -2.5]
fila3 = [7.3, -0.9, 0.2]
producto_escalar = np.dot(a,b)
producto_punto_a_b = np.multiply(a, b)
A= np.array([fila1, fila2, fila3])
A_transpuesta_1 = np.transpose(A)
arr_ones = np.ones((2, 3))
# Crear un array de 2x3 con todos los elementos inicializados en 1
arr_decimal = np.array([3.14159, 2.71828, 1.41421])
# Crear un array con números decimales
arr_rounded = np.round(arr_decimal, decimals=2)
# Redondear los elementos del array a 2 decimales
arr_decimal1 = np.array([3.2, 5.7, 8.1])
# Crear un array con números decimales
arr_ceil = np.ceil(arr_decimal1)
# Calcular el techo de cada elemento del array
arr_floor = np.floor(arr_decimal1)
# Calcular el piso de cada elemento del array
valor = A[0, 2]
# Definir el intervalo de valores de n
n_values = np.arange(0, 101)
# Calcular los valores de la función y[n]
y_values = np.sin(np.pi * 0.12 * n_values)
# Calcular los valores de la función y2[n]
y2_values = np.cos(2 * np.pi * 0.03 * n_values)
print("A) El producto punto de los vectores es:", producto_escalar)
print("B) El producto punto a punto de los vectores es:", producto_punto_a_b)
print("C) La matriz A, es:")
print(A)
print("D) La transpuesta de la matriz A (A^T) es:")
print(A_transpuesta_1)
print("E) Array de unos:")
print(arr_ones)
print("F) Array redondeado:")
print(arr_rounded)
print("G) Techo de cada elemento del array:")
print(arr_ceil)
print("H) Piso de cada elemento del array:")
print(arr_floor)
print("I) El valor de la primera fila, tercera columna de la matriz A es:", valor)
print("Acontinuación se muestra la gráfica de y[n] = sin(π * 0.12 * n)")
plt.figure()
plt.plot(n_values, y_values)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Gráfica de y[n] = sin(π * 0.12 * n)')
plt.grid(True)
plt.show()
plt.figure()
plt.plot(n_values, y2_values)
plt.xlabel('n')
plt.ylabel('y2[n]')
plt.title('Gráfica de y2[n] = cos(2π * 0.03 * n)')
plt.grid(True)
plt.show()
s_values = y_values + y2_values
t_values = y_values * y2_values

# Graficar y[n] y y2[n] en la misma figura
plt.figure()
plt.plot(n_values, y_values, label='y[n]', color='blue')
plt.plot(n_values, y2_values, label='y2[n]', color='red')
plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Gráfica de y[n] y y2[n]')
plt.legend()
plt.grid(True)
plt.show()

# Graficar s[n] y t[n] en la misma figura
plt.figure()
plt.plot(n_values, s_values, label='s[n] = y[n] + y2[n]', color='green')
plt.plot(n_values, t_values, label='t[n] = y[n] * y2[n]', color='purple')
plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Gráfica de s[n] y t[n]')
plt.legend()
plt.grid(True)
plt.show()
print("Adiós Mundo")