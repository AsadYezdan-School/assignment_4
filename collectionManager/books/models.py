from django.db import models

# Create your models here.
class testTable(models.Model):
    #put the data fields here
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
