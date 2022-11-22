from django.shortcuts import render
from .models import Alumnos, Inasistencias, Cursos
# Create your views here.

estudiantes = Alumnos.objects.all()
inasistencias = Inasistencias.objects.all()

def datos(division):
    for i in Alumnos.objects.filter(curso=division):
        print(type(i.curso))
    lista_alumnos = []
    for alumno in Alumnos.objects.filter(curso=division):
        faltas_totales = 0
        faltas_justificadas = 0
        tardes = 0
        fechas_totales = []
        fechas_justificadas = []
        fechas_tardes = []
        fechas_tardes_justificadas = []
        for i in Inasistencias.objects.filter(alumno=alumno):
            if i.tarde == False:
                faltas_totales +=1
                fechas_totales.append(i.fecha)
                if i.justificada:
                    fechas_justificadas.append(i.fecha)
                    faltas_justificadas += 1
            else:
                tardes += 1
                faltas_totales +=0.5
                fechas_tardes.append(i.fecha)
                if i.justificada:
                    fechas_tardes_justificadas.append(i.fecha)
                

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
        
        if len(fechas_tardes) == 0:
            fechas_tardes = "-"
        else:
            for i in fechas_tardes:
                fechas_tardes[fechas_tardes.index(i)] = str(i)
            fechas_tardes= str(fechas_tardes)[1:-1].replace("'","").replace("-", "/").replace(","," - ")
        
        if len(fechas_tardes_justificadas) == 0:
            fechas_tardes_justificadas = "-"
        else:
            for i in fechas_tardes_justificadas:
                fechas_tardes_justificadas[fechas_tardes_justificadas.index(i)] = str(i)
            fechas_tardes_justificadas= str(fechas_tardes_justificadas)[1:-1].replace("'","").replace("-", "/").replace(","," - ")

        diccionario = {
            "dni": alumno.dni,
            "nombre": alumno.nombre_completo(),
            "faltas_totales": faltas_totales,
            "faltas_justificadas": faltas_justificadas,
            "cant_tardes": tardes,
            "fechas_totales": fechas_totales,
            "fechas_justificadas": fechas_justificadas,
            "fechas_tardes": fechas_tardes,
            "fechas_tardes_justificadas": fechas_tardes_justificadas,                
        }
        lista_alumnos.append(diccionario)
    return lista_alumnos

def links():
    
    lista_cursos = []
    for i in Cursos.objects.all():
        lista_cursos.append(f"{i}")
    return lista_cursos

def index(request):
    return render(request, "index.html", {"links": links()})

def pagCurso(request, curso):
    division = Cursos.objects.get(año=curso[0], division=str(curso[1]).upper())
    return render(request, 'modelo.html', {"lista":datos(division=division), "division": division, "links": links()})

