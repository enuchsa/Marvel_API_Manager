from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    image = models.CharField(max_length=300, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']