from datetime import *

class ManejoFechas:
    def __init__(self, fecha_str):
        self.fecha = datetime.strptime(fecha_str, "%Y-%m-%d")

    def obtener_dia_semana(self):
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return dias_semana[self.fecha.weekday()]

    def sumar_dias(self, dias):
        nueva_fecha = self.fecha + timedelta(days=dias)
        return nueva_fecha.strftime("%Y-%m-%d")

    def calcular_diferencia(self, otra_fecha_str):
        otra_fecha = datetime.strptime(otra_fecha_str, "%Y-%m-%d")
        diferencia = abs(otra_fecha - self.fecha)

        # Extraer años, meses y días de la diferencia
        anos = diferencia.days // 365
        meses = (diferencia.days % 365) // 30
        dias = (diferencia.days % 365) % 30

        return anos, meses, dias

# Ejemplo de uso
fecha_ingresada = input("Ingrese una fecha en formato YYYY-MM-DD: ")
manejo_fechas = ManejoFechas(fecha_ingresada)

fecha_otra = input("Ingrese otra fecha en formato YYYY-MM-DD: ")
anos, meses, dias = manejo_fechas.calcular_diferencia(fecha_otra)

print(f"La diferencia de tiempo es de {anos} años, {meses} meses y {dias} días.")


tiempo = datetime.datetime.now()

print(tiempo)
print(tiempo.year)
print(tiempo.month)
print(tiempo.day)
print(tiempo.minute)
print(tiempo.second)
print(tiempo.microsecond)

print("hoy es {} de el mes {} en el año {}".format(tiempo.day,tiempo.month,tiempo.year))
 