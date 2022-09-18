from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    @property
    def fullname(self):
        full_name = "{ first_name } { last_name }".format(
            first_name=self.first_name,
            last_name=self.last_name
        )
        return full_name.strip()
