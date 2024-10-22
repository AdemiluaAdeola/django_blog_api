from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    #is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    status_choices = (
        ("Incomplete", "Incomplete"),
        ("Complete", "Complete"),
    )

    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    bio = models.TextField()
    whatsapp = models.PositiveBigIntegerField()
    telegram = models.PositiveBigIntegerField()
    instagram = models.URLField()
    twitter = models.URLField()
    status = models.CharField(max_length=255, choices=status_choices)

    def __str__(self):
        return self.user.username + "'s profile"