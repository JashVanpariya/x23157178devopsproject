from django.db import models

import uuid

class Player(models.Model):

    player_name = models.CharField(max_length=200)

    player_email = models.EmailField()

    player_contact = models.CharField(max_length=20)

    player_profession = models.CharField(max_length=200)

    player_salary = models.IntegerField()

id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

def __str__(self):

    return self.player_name
