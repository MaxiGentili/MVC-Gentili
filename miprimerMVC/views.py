from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template

def hola (request):
    return HttpResponse('Bueeenas')

def calcular_fecha_nacimiento (request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nac. aprox. es para tus {edad} años sería: {fecha}')

def mi_template (request):
    
    cargar_archivo = open(r"C:\Users\Maximiliano\Desktop\Coder House\Python\Clase 17  - Django - Portfolio (parte 1)\MVC\Proyecto\templates\template.html", "r")
    
    template = Template(cargar_archivo.read())
    
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)