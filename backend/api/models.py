from django.db import models

from django.utils.timezone import now

# Create your models here.

class Topics(models.Model):
    title =  models.CharField(max_length=250)
    
    subtitle = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateField(default=now)

    def __str__(self):
        return self.title