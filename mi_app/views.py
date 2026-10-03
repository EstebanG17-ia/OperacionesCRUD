from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto


def inicio(request):
    productos = Producto.objects.all().order_by('-id')
    return render(request, 'mi_app/index.html', {
        'productos': productos
    })


def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        descripcion = request.POST.get('descripcion', '').strip()
        precio = request.POST.get('precio', '')
        stock = request.POST.get('stock', '')

        if not nombre or not precio or not stock:
            messages.error(request, 'Completa los campos obligatorios.')
            return render(request, 'mi_app/formulario.html', {
                'titulo': 'Registrar producto',
                'producto': request.POST
            })

        try:
            precio = float(precio)
            stock = int(stock)

            if precio < 0 or stock < 0:
                raise ValueError

            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock
            )
            messages.success(request, 'Producto registrado correctamente.')
            return redirect('inicio')

        except (ValueError, TypeError):
            messages.error(request, 'Ingresa un precio y stock válidos.')

    return render(request, 'mi_app/formulario.html', {
        'titulo': 'Registrar producto'
    })


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        descripcion = request.POST.get('descripcion', '').strip()
        precio = request.POST.get('precio', '')
        stock = request.POST.get('stock', '')

        if not nombre or not precio or not stock:
            messages.error(request, 'Completa los campos obligatorios.')
        else:
            try:
                precio = float(precio)
                stock = int(stock)

                if precio < 0 or stock < 0:
                    raise ValueError

                producto.nombre = nombre
                producto.descripcion = descripcion
                producto.precio = precio
                producto.stock = stock
                producto.save()

                messages.success(request, 'Producto actualizado correctamente.')
                return redirect('inicio')

            except (ValueError, TypeError):
                messages.error(request, 'Ingresa un precio y stock válidos.')

    return render(request, 'mi_app/formulario.html', {
        'titulo': 'Editar producto',
        'producto': producto
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')

    return redirect('inicio')