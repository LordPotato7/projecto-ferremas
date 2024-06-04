from django.urls import path, include
from .views import home, martillos, contactos, agregar, listarP, modificar_producto, eliminar_producto, registro, login, ProductoViewset, listarU, UserViewset, agregarOferta
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('user', UserViewset)
  

urlpatterns = [
    path('', home, name="home"),
    path('martillos', martillos, name="martillos"),
    path('contactos', contactos, name="contactos"),
    path('agregar', agregar, name="agregar"),
    path('listarP', listarP, name="listarP"),
    path('modificarP/<id>', modificar_producto, name="modificarP"),
    path('eliminarP/<id>', eliminar_producto, name="eliminarP"),
    path('registro', registro, name="registro"),
    path('login', login, name="login"),
    path('api/', include(router.urls)),
    path('listarU', listarU, name="listarU" ),
    path('agregarOferta', agregarOferta, name="agregarOferta")
    
    
]

