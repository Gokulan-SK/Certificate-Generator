from django.db import models

# Create your models here.
class CompletedGeneration(models.Model):
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    duration = models.CharField(max_length=30)
    email = models.EmailField()
    generation_time = models.DateTimeField(auto_now_add=True)
    certificate = models.BinaryField(null=True)
    def __str__(self):
        return self.name+'\'certificate for '+self.course
    
    