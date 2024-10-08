from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
