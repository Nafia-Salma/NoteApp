from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="créé à", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="mis à jour à", null=True)

    class Meta:
        abstract = True
