import math

# Definir las variables y sus incertidumbres
m = 10.8    # masa medida en gramos
dm = 0.1    # incertidumbre en la masa en gramos
r = 0.035   # radio medido en metros
dr = 0.001  # incertidumbre en el radio en metros
h = 0.81    # distancia medida en metros
dh = 0.01   # incertidumbre en la distancia en metros
g = 9.8     # aceleración debido a la gravedad en m/s^2

# Calcular el promedio del tiempo t barra
t = [3.40, 3.45, 3.47, 4.13, 3.92, 3.85, 3.05, 3.52, 3.94, 2.89,
     2.94, 2.55, 3.12, 3.17, 4.06, 2.97, 3.23, 4.20, 3.24, 3.60,
     3.59, 3.65, 3.55, 3.07, 3.61, 3.61, 3.54, 3.76, 3.37, 3.57]
t_barra = sum(t) / len(t)

# Calcular el momento de inercia y su incertidumbre
I = m * r**2 * ((g * t_barra**2 / (2 * h)) - 1)
dI = math.sqrt((r**2 * ((g * t_barra**2 / (2 * h)) - 1))**2 * dm**2 +
               (2 * m * r * ((g * t_barra**2 / (2 * h)) - 1))**2 * dr**2 +
               (m * r**2 * (g * t_barra / (h * (2 * h - 1))))**2 * dh**2)

# Convertir a g m^2
I_g_m2 = I * 1e3
dI_g_m2 = dI * 1e3

# Imprimir el resultado en g m^2
print("Momento de inercia I':", I_g_m2, "g m^2")
print("Incertidumbre en I':", dI_g_m2, "g m^2")

