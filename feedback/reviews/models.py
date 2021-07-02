from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class ReviewModel(models.Model):
    user_name=models.CharField(max_length=50)
    review_text=models.TextField(max_length=100)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return str(self.id)
    

    class Meta:
        verbose_name_plural="Reviews"
