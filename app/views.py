from django.shortcuts import render, get_object_or_404
from .models import Producto, Contacto, Producto_Oferta
from .forms import ContactoForm, ProductoForm,CustomUserCreationForm, ProductoOfertaForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer,UserSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer 

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

# Create your views here.
def home(request):
    productosOferta = Producto_Oferta.objects.all()

    data = {
        'productosOferta' : productosOferta
    }
    return render(request,'app/home.html', data)

def martillos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request,'productos/herramientas/martillos.html',data)

def contactos(request):

    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Mensaje enviado correctamente'
        else :
            data['form'] = formulario
    return render(request,'app/contacto.html', data)


#Producto normal
@permission_required('app.add_producto')
def agregar(request):
    data = { 
        'form': ProductoForm()
    }

    if request.method== 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Modificado Correctamente")
        else:
            data["form"]=formulario
    return render(request,'formularios/agregar.html', data)

@permission_required('app.view_producto')
def listarP(request):

    productos = Producto.objects.all()


    data = {
        'productos' : productos
    }

    return render(request,'formularios/listar.html', data)


@permission_required('app.change_producto')
def modificar_producto (request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method== 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Modificado Correctamente")
            return redirect(to='listarP')
        else:
            data["form"]=formulario

    return render(request, 'formularios/modificar.html',data)

@permission_required('app.delete_producto')
def eliminar_producto (request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")

    return redirect(to='listarP')

#Usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            user = authenticate(request, username=usuario.username, password=formulario.cleaned_data["password1"])
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Te has registrado correctamente")
                return redirect('home')
        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)


def login(request):
    return render(request, 'registration/login.html')


@permission_required('app.view_producto')
def listarU(request):

    usuarios = User.objects.all()

    data = {
        'usuarios' : usuarios
    }
    return render(request,'formularios/listarU.html', data)


def eliminar_usuario (request, id):

    usuario = User.objects.get(id=id)
    usuario.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to='listarU')

#Agregar Oferta


def agregarOferta(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    # Initialize the data dictionary here
    data = {} 
    
    # Pass initial data to the form based on the product
    initial_data = {
        'codigo' : producto.codigo if hasattr(producto, 'codigo') else None,
        'nombre': producto.nombre if hasattr(producto, 'nombre') else None,
        'tipo': producto.tipo if hasattr(producto, 'tipo') else None,
        'marca': producto.marca if hasattr(producto, 'marca') else None,
        'stock': producto.stock if hasattr(producto, 'stock') else None,
        'precio': producto.precio if hasattr(producto, 'precio') else None,
        'imagen': producto.imagen if hasattr(producto, 'imagen') else None,
        'stock': producto.stock if hasattr(producto, 'stock') else None,
        'categoria': producto.categoria if hasattr(producto, 'categoria') else None,
    }
    
    if request.method == 'POST':
        formulario = ProductoOfertaForm(data=request.POST, files=request.FILES, initial=initial_data)
        if formulario.is_valid():
            # Associate the offer with the product
            oferta = formulario.save(commit=False)
            oferta.producto = producto
            oferta.save()
            
            messages.success(request, " Modificado Correctamente")
            return redirect(to='listarP')
        else:
            data["form"] = formulario
    else:
        data['form'] = ProductoOfertaForm(initial=initial_data)
    
    return render(request,'formularios/oferta/agregarOferta.html', data)
def listarOferta(request):

    productosOferta = Producto_Oferta.objects.all()

    data = {
        'productosOferta' : productosOferta
    }

    return render(request,'formularios/oferta/listarOferta.html', data)
