from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title
