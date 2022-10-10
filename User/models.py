from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.


class User(AbstractUser):
    """User model"""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=12, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()


