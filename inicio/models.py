from django.db import models

class Planta(models.Model):
    especie = models.CharField(max_length=25)
    habitat = models.CharField(max_length=18)

    def __str__(self):
        
        return f'{self.especie} {self.habitat}'
