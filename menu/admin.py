from django.contrib import admin
from .models import Venta

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'medio_pago', 'fecha_hora') # Adapta según tus campos
    list_filter = ('curso_cajero', 'turno', 'medio_pago')
    search_fields = ('cliente', 'cajero__username')
    ordering = ('-fecha_hora',)

# Registro directo al final del archivo
admin.site.register(Venta, VentaAdmin)