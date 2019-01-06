from django.db import models

# Create your models here.
class City(models.Model):
    #Objective: To be able to store city names in table
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
