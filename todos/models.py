from django.db import models


# Create your models here.
class Task(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=200)
    is_done = models.BooleanField()

    def __str__(self):
        return f'{self.text} from {self.date_created} is {self.is_done}'
