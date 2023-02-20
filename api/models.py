from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    
    def __str__(self):
        return self.title
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal , on_delete=models.CASCADE) 
    user = models.ForeignKey(User , on_delete=models.CASCADE)   
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    def __str__(self):
        return f"{self.meal.title} - {self.user.username}"
    
    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)
