fechas_totales = ["datetime.date(2022, 11, 12)", "datetime.date(2022, 11, 9)"]

for i in fechas_totales:
    fechas_totales[fechas_totales.index(i)] = i[14:-1]
    print(i)
print(fechas_totales)