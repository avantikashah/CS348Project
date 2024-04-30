from django.contrib import admin

# Register your models here.
from .models import FoodOption
admin.site.register(FoodOption)
from .models import FoodPreference
admin.site.register(FoodPreference)
from .models import FoodWaste
admin.site.register(FoodWaste)
