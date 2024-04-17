import matplotlib.pyplot as plt
import numpy as np

# Definir los puntos
origen = (0, 0)
v1 = (0, -8)
v2 = (1, -8)
v3 = (1, -6)

# Extraer las coordenadas x e y de los puntos
x = [p[0] for p in [origen, v1, v2, v3]]
y = [p[1] for p in [origen, v1, v2, v3]]

# Crear la gráfica
plt.figure(figsize=(8, 6))

# Dibujar los puntos
plt.plot(x, y, 'o')

# Dibujar los vectores
plt.quiver([origen[0], v1[0], v2[0]], [origen[1], v1[1], v2[1]], 
           [v1[0]-origen[0], v2[0]-v1[0], v3[0]-v2[0]], 
           [v1[1]-origen[1], v2[1]-v1[1], v3[1]-v2[1]],
           angles='xy', scale_units='xy', scale=1, color=['r', 'g', 'b'],
           label=['V1', 'V2', 'V3'])

# Etiquetas de los puntos
for i, txt in enumerate(['Origen', 'V1', 'V2', 'V3']):
    plt.annotate(txt, (x[i], y[i]), xytext=(5, -5), textcoords='offset points')

# Calcular y dibujar los ángulos
angle1 = np.arctan2(v1[1], v1[0]) * 180 / np.pi
angle2 = np.arctan2(v2[1] - v1[1], v2[0] - v1[0]) * 180 / np.pi

plt.annotate('', xy=(0, 0), xytext=(0.4, -7), arrowprops=dict(facecolor='black', arrowstyle='<->'))
plt.annotate('Ángulo: {:.2f}°'.format(angle1), xy=(0.2, -7), xytext=(0.6, -7), fontsize=10)

plt.annotate('', xy=(v1[0], v1[1]), xytext=(v2[0], v2[1]), arrowprops=dict(facecolor='black', arrowstyle='<->'))
plt.annotate('Ángulo: {:.2f}°'.format(angle2), xy=(0.5, -8), xytext=(0.9, -8), fontsize=10)

# Título y leyenda
plt.title('Gráfica de Vectores')
plt.legend()

# Mostrar la gráfica
plt.grid()
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
