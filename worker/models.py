from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100, default = '')
    type = models.CharField(max_length=100, default ='')
    input_data = models.CharField(max_length=100)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name