from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete= models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='productos', null=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Producto_Oferta(models.Model):

    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    stock = models.IntegerField()
    fecha = models.DateField(auto_now=True)
    precio = models.IntegerField()
    precio_oferta = models.IntegerField()
    imagen = models.ImageField(upload_to='productos oferta', null=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

opciones_consulta = [
    [0,"consulta"],
    [1,"sugerencia"],
    [2,"reclamo"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices= opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()


    def __str__(self):
        return self.nombre