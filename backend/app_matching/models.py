from django.db import models

class Element(models.Model):
    nombre = models.CharField(max_length=50)
    peso = models.IntegerField()
    calorias = models.IntegerField()

    def __str__(self):
        return self.nombre

class Combination(models.Model):
    elementos = models.ManyToManyField(Element)
    total_peso = models.IntegerField()
    total_calorias = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Combinación {self.id} - Peso: {self.total_peso}, Calorías: {self.total_calorias}"
