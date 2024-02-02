from django.db import models

# Create your models here.
class CertificateData(models.Model):
    firstname = models.CharField(max_length=255)

    def __str__(self):
        return self.title  # Display the title when the model instance is printed