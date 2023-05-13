from django.db import models

# Create your models here.
class Data(models.Model):
    data = models.CharField(max_length=100)
    value = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Data Visualization'

    def __str__(self):
        return f'{self.data}-{self.value}'