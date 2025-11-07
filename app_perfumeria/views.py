from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Producto
import datetime

# -----------------------
# PÁGINA INICIO
# -----------------------
def inicio_perfumeria(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'inicio.html', context)

# ====================================================
# CRUD: EMPELADO (se deja igual que tenías)
# ====================================================
def ver_empleado(request):
    empleados = Empleado.objects.all().order_by('id')
    return render(request, 'empleado/ver_empelado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        puesto = request.POST.get('puesto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_contratacion = request.POST.get('fecha_contratacion') or None

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            puesto=puesto,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            activo=True
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empelado.html')

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'empleado/actualizar_empelado.html', {'empleado': empleado})

def realizar_actualizacion_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        empleado.puesto = request.POST.get('puesto')
        empleado.telefono = request.POST.get('telefono')
        empleado.email = request.POST.get('email')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion') or None
        activo_val = request.POST.get('activo')
        empleado.activo = True if activo_val == 'on' else False
        empleado.save()
        return redirect('ver_empleado')
    return redirect('actualizar_empleado', empleado_id=empleado.id)

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empelado.html', {'empleado': empleado})


# ====================================================
# CRUD: PRODUCTO (nuevo)
# ====================================================
def ver_producto(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'producto/ver_producto.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio') or 0.00
        stock = request.POST.get('stock') or 0
        categoria = request.POST.get('categoria')
        sku = request.POST.get('sku')

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            sku=sku,
            activo=True
        )
        return redirect('ver_producto')
    return render(request, 'producto/agregar_producto.html')

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})

def realizar_actualizacion_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio') or producto.precio
        producto.stock = request.POST.get('stock') or producto.stock
        producto.categoria = request.POST.get('categoria')
        producto.sku = request.POST.get('sku')
        activo_val = request.POST.get('activo')
        producto.activo = True if activo_val == 'on' else False
        producto.save()
        return redirect('ver_producto')
    return redirect('actualizar_producto', producto_id=producto.id)

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})
