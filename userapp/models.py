from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.CharField(max_length=500,default = 'https://images.unsplash.com/photo-1526779259212-939e64788e3c?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZnJlZSUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D&fm=jpg&q=60&w=3000')

    def __str__(self):
        return self.name     