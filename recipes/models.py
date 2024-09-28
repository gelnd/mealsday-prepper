from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    units = models.CharField(max_length=10, help_text="Unit of measure (cups, oz, ets)")

    def __str__(self) -> str:
        return f"{self.quantity} {self.units} of {self.name}"

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    instructions = models.TextField()
    cook_time = models.IntegerField(help_text="Time to cook (minutes)")
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self) -> str:
        return self.title
