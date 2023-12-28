from django.db import models

from heroes.hero.models import Hero

class Group(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    heroes = models.ForeignKey(Hero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']