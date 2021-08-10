from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Nombre', max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, default=None, verbose_name='Categoría padre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Supplier(models.Model):
    name = models.CharField('Nombre', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Product(models.Model):
    name = models.CharField('Nombre', max_length=255)
    unit_price = models.FloatField('Precio Unitario')
    unit_per_package = models.FloatField('Unidades por bulto')
    package_price = models.FloatField('Costo por bulto')
    active = models.BooleanField('Activo', default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
