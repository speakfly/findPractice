from django.db import models

# Create your models here.
class User(models.Model):
    emial = models.EmailField()
    position = models.CharField(max_length=20, default="实习 java")
    addr = models.CharField(max_length=20, default="广州")
    salary = models.IntegerField(default=3000)

    def __str__(self):
        return self.emial
