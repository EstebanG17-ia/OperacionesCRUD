from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_1 = models.CharField(max_length=50)
    tipo_2 = models.CharField(max_length=50, blank=True, null=True)  # blank=True y null=True permiten que sea opcional
    vida = models.IntegerField()
    ataque = models.IntegerField()
    defensa = models.IntegerField()

    def __str__(self):
        return self.nombre