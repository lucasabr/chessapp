from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Game(models.Model):
    date_played = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET("DeletedUser"))
    
    def __str__(self):
        return self.author