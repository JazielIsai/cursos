# Una empresa ha encargado un programa para calcular las nóminas de los trabajadores.
# 1) El sueldo base semanal sale aplicando la siguiente fórmula: horastrabajo * preciohora + horesextra*preciohoraextra
# 2) El preciohora es una constante=6.
# El preciohoraextra depende de las h.extra hechas: si son menos de 10h extras
# semanales, el precio es un 50% mayor que el preciohora (* 1,5). Si se hacen entre 10 y 20h extra,
# el precio es un 40% mayor. Si se hacen más de 20h, el precio es un 20% mayor.
# 3) Si el trabajador es de categoría 3, el preciohora es el constante.
# 4) Si es de categoría 2; el preciohora es un 25% mayor y si es de categoría 1 es un 45% más


def calculate_base_salary(hour_work, precious_hour, extra_hours, precious_extra_hours):
    return (hour_work * precious_hour) + (extra_hours * precious_extra_hours)


def calculate_extra_hours(extra_hours, precious_hour):
    precious_extra_hours = 0
    if extra_hours < 10:
        precious_extra_hours = precious_hour * 1.5
    elif extra_hours > 10 and extra_hours < 20:
        precious_extra_hours = precious_hour * 1.3
    elif extra_hours > 20:
        precious_extra_hours = precious_hour * 1.2

    return precious_extra_hours


def category_personal(category):
    precious_hour = 0
    if category == 3:
        precious_hour = 6
    elif category == 2:
        precious_hour = 7.5
    elif category == 1:
        precious_hour = 8.7

    return precious_hour


print('El total es: ')
print(calculate_base_salary(4, category_personal(3), 12, calculate_extra_hours(12, category_personal(3))))
