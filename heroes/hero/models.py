from django.db import models

from heroes.group.models import Group


class Hero(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    image = models.CharField(max_length=300, null=False, blank=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='heroes', null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']