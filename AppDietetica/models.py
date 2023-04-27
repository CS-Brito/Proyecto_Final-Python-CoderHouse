from django.db import models

class usuario(models.Model):
    user = models.CharField(max_length=40)
    password = models.CharField(max_length=10)
    
class pedido(models.Model):
    fecha_pedido = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
    direccion_entrega = models.CharField(max_length=100)
    codig_postal_entrega= models.CharField(max_length=20)
    total = models.FloatField()
    pagado = models.BooleanField()
    
class producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=200)
    precio_unitario = models.FloatField()
    stock = models.BooleanField()
    
class categoriaProducto(models.Model):
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)
    
class cliente(models.Model):
    apellido = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150)
    codig_postal= models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    
class carrito(models.Model):
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    subtotal = models.FloatField()
