from django.shortcuts import render
from .models import Alumnos, Inasistencias
# Create your views here.

estudiantes = Alumnos.objects.all()
inasistencias = Inasistencias.objects.all()

def datos(division):
    lista_alumnos = []
    for alumno in estudiantes:
        if alumno.curso == division:
            faltas_totales = 0
            faltas_justificadas = 0
            fechas_totales = []
            fechas_justificadas = []
            for i in inasistencias:
                if i.alumno == alumno:
                    faltas_totales +=1
                    fechas_totales.append(i.fecha)
                    if i.justificada:
                        fechas_justificadas.append(i.fecha)
                        faltas_justificadas += 1

            if len(fechas_totales) == 0:
                fechas_totales = "-"
            else:
                for i in fechas_totales:
                    fechas_totales[fechas_totales.index(i)] = str(i)
                fechas_totales = str(fechas_totales)[1:-1].replace("'","").replace("-", "/").replace(","," - ")

            if len(fechas_justificadas) == 0:
                fechas_justificadas = "-"
            else:
                for i in fechas_justificadas:
                    fechas_justificadas[fechas_justificadas.index(i)] = str(i)
                fechas_justificadas = str(fechas_justificadas)[1:-1].replace("'","").replace("-", "/").replace(","," - ")

            diccionario = {
                "dni": alumno.dni,
                "nombre": alumno.nombre_completo(),
                "faltas_totales": faltas_totales,
                "faltas_justificadas": faltas_justificadas,
                "fechas_totales": fechas_totales,
                "fechas_justificadas": fechas_justificadas                
            }
            lista_alumnos.append(diccionario)
    return lista_alumnos

def index(request):
    return render(request, "index.html")

def quintoA(request):
    return render(request, 'modelo.html', {"lista":datos("5A"), "division": "5A"})

def quintoB(request):
    return render(request, 'modelo.html', {"lista":datos("5B"), "division": "5B"})

def cuartoA(request):
    return render(request, 'modelo.html', {"lista":datos("4A"), "division": "4A"})

def cuartoB(request):
    return render(request, 'modelo.html', {"lista":datos("4B"), "division": "4B"})

def terceroA(request):
    return render(request, 'modelo.html', {"lista":datos("3A"), "division": "3A"})

def terceroB(request):
    return render(request, 'modelo.html', {"lista":datos("3B"), "division": "3B"})

def segundoA(request):
    return render(request, 'modelo.html', {"lista":datos("2A"), "division": "2A"})

def segundoB(request):
    return render(request, 'modelo.html', {"lista":datos("2B"), "division": "2B"})

def primeroA(request):
    return render(request, 'modelo.html', {"lista":datos("1A"), "division": "1A"})

def primeroB(request):
    return render(request, 'modelo.html', {"lista":datos("1B"), "division": "1B"})