from django import forms
from .models import FoodPreference
from .models import FoodWaste
from.models import FoodOption

class FoodPreferenceForm(forms.ModelForm):
    class Meta:
        model = FoodPreference
        fields = ['student_name', 'is_vegetarian', 'is_vegan', 'favorite_food']

class FoodOptionsForm(forms.ModelForm):
    class Meta:
        model = FoodOption
        fields = ['food_name', 'veg', 'vegan', 'gluten_free']
    
class FoodWasteForm(forms.ModelForm):
    class Meta:
        model = FoodWaste
        fields = ['date_served', 'food', 'meal', 'waste_amount']
        
class FoodSpecificReportForm(forms.Form):
    food_name = forms.ModelChoiceField(queryset=FoodOption.objects.all(), empty_label=None)
    month = forms.IntegerField(min_value=1, max_value=12)
    year = forms.IntegerField(min_value = 2000, max_value = 2024)
    
class GeneralReportForm(forms.Form):
    month = forms.IntegerField(min_value=1, max_value=12)
    year = forms.IntegerField(min_value = 2000, max_value = 2024)
    min_waste = forms.IntegerField(label="Minimum Waste Amount", required=False)
    max_waste = forms.IntegerField(label="Maximum Waste Amount", required=False)

    
