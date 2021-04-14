from django.db import models

# Create your models here.

class Contracte(models.Model):
    codi = models.TextField()
    denominacio = models.TextField()
    codi_expedient = models.TextField()
    objecte = models.TextField()
    pressupost = models.FloatField()
    valor_estimat = models.FloatField()
    lloc_execucio = models.TextField()
    duracio = models.TextField()
    termini_presentacio_instancies = models.DateField()
    tipus = models.TextField()
    subtipus = models.TextField()
    # dataAdjudicacio = models.ForeignKey(Lot, on_delete=models.CASCADE)
    # dataFormalitzacio = models.ForeignKey(Lot, on_delete=models.CASCADE)
    # lots = models.ManyToManyField(Lot)
    #anuncisFases = models.ForeignKey(AnunciFase, on_delete=models.CASCADE)

    def __str__(self):
        return self.denominacio