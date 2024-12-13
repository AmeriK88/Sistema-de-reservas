from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15, blank=True, null=True)
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    numero_habitaciones = models.PositiveIntegerField(default=1)
    numero_huespedes = models.PositiveIntegerField()
    estado = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')],
        default='pending'
    )
    
    def clean(self):
        # Validación personalizada para fechas
        if self.fecha_salida <= self.fecha_llegada:
            raise ValidationError("La fecha de salida debe ser posterior a la fecha de llegada.")
        
        if self.fecha_llegada < date.today():
            raise ValidationError("La fecha de llegada no puede ser anterior a hoy.")
        
        # Validación para el número de habitaciones y huéspedes
        if self.numero_huespedes > self.numero_habitaciones * 4:  # Asumiendo 4 huéspedes por habitación
            raise ValidationError("El número de huéspedes excede la capacidad de las habitaciones seleccionadas.")
        
        # Validación de estado
        if self.estado not in ['pending', 'confirmed', 'canceled']:
            raise ValidationError("El estado de la reserva es inválido.")
    
    def __str__(self):
        return f"Reserva de {self.nombre_cliente}: {self.fecha_llegada} - {self.fecha_salida}, {self.numero_habitaciones} habitación(es)"
