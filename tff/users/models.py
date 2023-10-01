from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        ("username"),
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
class Post(models.Model):
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    user_pop= models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.text