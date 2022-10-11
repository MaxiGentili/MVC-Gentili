from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random

from home.models import Persona


def crear_personas(request):
    
    # persona = Persona(nombre=nombre, apellido='Gentili', edad=int(45), fecha_nacimiento=datetime.now())
    persona1 = Persona(nombre='Gustavo', apellido='Gentili', edad=int(45), fecha_nacimiento=datetime.now())
    persona2 = Persona(nombre='Silvana', apellido='Marcello', edad=random.randrange(1, 70), fecha_nacimiento=datetime.now())
    persona3 = Persona(nombre='Carolina', apellido='Nazar', edad=random.randrange(1, 70), fecha_nacimiento=datetime.now())
    # persona.save()
    persona1.save()
    persona2.save()
    persona3.save()
    
    template = loader.get_template('crear_personas.html')
    # template_renderizado = template.render()
    template_renderizado = template.render({})
    
    return HttpResponse(template_renderizado)


def ver_personas(request):
      
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    
    return HttpResponse(template_renderizado)