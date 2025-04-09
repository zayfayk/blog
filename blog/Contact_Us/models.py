from django.db import models
from django.core.validators import RegexValidator

class Forms(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,25}$',  # This pattern matches numbers with optional "+" and 9-15 digits
        message="Phone number must be entered in the format: '+999999999'. Up to 25 digits allowed."
    )
    phone = models.CharField(validators=[phone_validator], max_length=25)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
