from django.db import models
from django.utils import timezone


# Create your models here.
class Workshop(models.Model):
    Name = models.CharField(max_length=255)
    Detail = models.TextField()
    Location = models.TextField()
    Slot  = models.IntegerField()
    Date = models.DateTimeField(default=timezone.now)
    Prize = models.IntegerField()

    def __str__(self):
        return self.Name

class Admission(models.Model):
    CERTIFICATION=[
        ('Y','YES'),
        ('N','NO')
    ]
    Name = models.CharField(max_length=255)
    Desc = models.TextField()
    Duration = models.CharField(max_length=255)
    Mode = models.CharField(max_length=255)
    Fees = models.IntegerField()
    Certifiction = models.CharField(max_length=5,choices=CERTIFICATION)

    def __str__(self):
        return self.Name


class Reviews(models.Model):
    Name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.Name