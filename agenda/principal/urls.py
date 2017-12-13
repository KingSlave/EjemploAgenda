from django.conf.urls import url
from views import *


urlpatterns = [
url(r'cerrarSesion/$',cerrarSesion),
url(r'autenticar/$',autenticar),
url(r'login/$',login),
url(r'feliminar/$',feliminar),
url(r'eliminar/$',eliminar),
url(r'guardarCambios/$',guardarCambios),
url(r'modificar/$',modificar),
url(r'consultar/$',consulta),
url(r'guardar/$',insertar),
url(r'nuevo/$',insertar),
url(r'sumar/$',sumar),
url(r'^p1/$',pagina1),
url(r'^p2/$',pagina2),
url(r'^saludo/$',saludo),
url(r'^$',index)
]
