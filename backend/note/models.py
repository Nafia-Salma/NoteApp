from colorfield.fields import ColorField
from django.db import models
from backend.models import BaseModel
from django.contrib.auth.models import User

class Note(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Titre")
    content = models.TextField(verbose_name="Contenu")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", verbose_name="Auteur")
    tags = models.ManyToManyField("Tag", related_name="notes", blank=True, verbose_name="Étiquettes")

    def __str__(self):
        return self.title


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nom de l'étiquette")
    color = ColorField(verbose_name="Couleur")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags", verbose_name="Auteur")  # Add author field


    def __str__(self):
        return self.name
