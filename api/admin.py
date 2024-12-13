from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nombre_cliente', 'fecha_llegada', 'fecha_salida', 'estado']
    list_filter = ['fecha_llegada', 'estado']
