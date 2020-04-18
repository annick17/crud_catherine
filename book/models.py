from django.db import models

# Create your models here.

class Book(models.Model):
    nom = models.CharField(max_length = 50)
    picture = models.ImageField()
    auteur = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    description = models.TextField(default = 'Vous devez entrer votre description ici !')
 
    def __str__(self):
        return self.name