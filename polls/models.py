from django.db import models
from django.contrib.postgres.indexes import HashIndex

class FoodOption(models.Model):
  food_name = models.CharField(max_length = 200)
  def __str__(self): 
         return self.food_name
  veg = models.BooleanField()
  vegan = models.BooleanField()
  gluten_free = models.BooleanField()
  #hash index
  class Meta:
       indexes = (HashIndex(fields= ('food_name',)),)
     
class FoodPreference(models.Model):
    student_name = models.CharField(max_length = 200)
    def __str__(self): 
         return self.student_name
    is_vegetarian = models.BooleanField()
    is_vegan = models.BooleanField()
    favorite_food = models.ForeignKey(FoodOption, on_delete=models.CASCADE)

class FoodWaste(models.Model):
    date_served = models.DateTimeField("date")
    def __str__(self): 
         x = str(self.date_served.date()) + " " + self.food.food_name + " " + self.meal
         return x
    food = models.ForeignKey(FoodOption, on_delete=models.CASCADE)    
    meal = models.CharField(max_length = 20)
    #b+ tree index
    waste_amount = models.IntegerField(default = 0, db_index = True)


