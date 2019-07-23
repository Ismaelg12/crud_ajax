from django.db import models

class Book(models.Model):

    id            = models.AutoField(primary_key=True)
    agenda        = models.DateField(null=True)
    hora_inicio   = models.TimeField(null=True)
    hora_fim      = models.TimeField(null=True)
    paciente      = models.CharField(max_length=50,blank=True)
    #paciente      = models.ForeignKey(Paciente,on_delete=models.PROTECT)

def __str__(self):
    return self.paciente