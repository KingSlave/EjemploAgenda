from django.shortcuts import render
from django.http import HttpResponse
from models import Persona
from django.views.decorators.cache import never_cache
# Create your views here.
@never_cache
def index(request):
    lista=[Persona(1,"Martha"),
           Persona(2,"Gabriela"),
           Persona(3,"Carlos")]

    return render(request,'index.html',{'nombre':'Pepe','lista':lista})
@never_cache
def saludo(request):
    return HttpResponse("Bienvenido a DJANGO")
@never_cache
def pagina1(request):
    return render(request,'pagina1.html')
@never_cache
def pagina2(request):
    return render(request,'pagina2.html')
@never_cache
def insertar(request):
    if 'id' in request.POST and 'nombre' in request.POST and 'email' in request.POST and 'tel' in request.POST:
        idPersona = request.POST['id']
        nombre = request.POST['nombre']
        email = request.POST['email']
        tel = request.POST['tel']
        p = Persona(idPersona=idPersona, nombre=nombre,email=email,telefono=tel)
        p.save()
        return render(request,'insertar.html')
    else:
        return render(request,'insertar.html')

@never_cache
def sumar(request):
    if 'num1' in request.POST and 'num2' in request.POST:
        n1 = request.POST['num1']
        n2 = request.POST['num2']
        suma  = int(n1) + int(n2)
        return render(request,'fsumar.html',{'res':suma,'n1':n1,'n2':n2})
    else:
        return render(request,'fsumar.html')

WAMP - Windows Apache MySQL Php




@never_cache
def consulta(request):
    registros = Persona.objects.all()
    return render(request,'consulta.html',{'registros':registros})
@never_cache
def modificar(request):
    registro = Persona.objects.get(idPersona=request.POST['id'])
    return render(request,'modificar.html',{'reg':registro})

@never_cache
def guardarCambios(request):
    p = Persona(idPersona = request.POST['id'])
    p.nombre = request.POST['nombre']
    p.email = request.POST['email']
    p.telefono = request.POST['tel']
    p.save()
    registros = Persona.objects.all()
    return render(request,'consulta.html',{'msg': 'Se ha actualizado el registro correctamente','registros':registros})

def eliminar(request):
    p = Persona(idPersona = request.POST['id'])
    p.delete()
    registros = Persona.objects.all()
    return render(request,'consulta.html',{'msg':'Registro eliminado','registros':registros})

def feliminar(request):
    id = request.GET['id']
    return render(request,'eliminar.html',{'id':id})
