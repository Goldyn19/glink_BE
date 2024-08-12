from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Links(models.Model):
    label = models.CharField(max_length=80)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.label} {self.link}"
# Create your models here.
