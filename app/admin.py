from django.contrib import admin
from .models import Categoria, Marca, Producto, Tipo,Producto_Oferta,Contacto

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Tipo)
admin.site.register(Producto_Oferta)
admin.site.register(Contacto)

