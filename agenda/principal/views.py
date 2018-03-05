from django.shortcuts import render
from django.http import HttpResponse
from models import Persona
from models import Usuario

# Create your views here.
def login(request):
    return render(request,'login.html')

def index(request):
    lista=[Persona(1,"Martha"),
           Persona(2,"Gabriela"),
           Persona(3,"Carlos")]

    return render(request,'index.html',{'nombre':'Pepe','lista':lista})

def saludo(request):
    return HttpResponse("Bienvenido a DJANGO")

def pagina1(request):
    return render(request,'pagina1.html')

def pagina2(request):
    return render(request,'pagina2.html')

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


def sumar(request):
    if 'num1' in request.POST and 'num2' in request.POST:
        n1 = request.POST['num1']
        n2 = request.POST['num2']
        suma  = int(n1) + int(n2)
        return render(request,'fsumar.html',{'res':suma,'n1':n1,'n2':n2})
    else:
        return render(request,'fsumar.html')


def consulta(request):
    if request.session.get('usuario','_anonimo')=='_anonimo':
        return login(request)
    registros = Persona.objects.all()
    return render(request,'consulta.html',{'registros':registros})

def modificar(request):
    registro = Persona.objects.get(idPersona=request.POST['id'])
    return render(request,'modificar.html',{'reg':registro})

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

def autenticar(request):
    if request.POST:
        try:
            u = Usuario.objects.get(usuario=request.POST['usuario'],password=request.POST['pass'])
        except Usuario.DoesNotExist as e:
            return render(request,'login.html',{'msg':'Datos incorrectos'})
        else:
            request.session['usuario'] = u.usuario
            return consulta(request)
    else:
        return login(request)

def cerrarSesion(request):
    del request.session['usuario']
    return login(request)
