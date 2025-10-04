from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateField(auto_now_add=True)


