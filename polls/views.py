from django.shortcuts import render, redirect
from .forms import FoodPreferenceForm
from .forms import FoodWasteForm
from .forms import FoodOptionsForm
from .forms import FoodSpecificReportForm
from .forms import GeneralReportForm
from .models import FoodPreference
from .models import FoodWaste
from .models import FoodOption
from django.db.models import Count, Sum
from django.db import transaction

# Create your views here.
from django.http import HttpResponse

# def reports(request):
#     return HttpResponse("Hello, this is where reports will be displayed.")

@transaction.atomic
def waste(request):
    if request.method == 'POST':
        form = FoodWasteForm(request.POST)
        if form.is_valid():
            form.save()
            # Render a success message
            success_message = "Food Waste added successfully!"
            return render(request, 'basic_form.html', {'form': FoodWasteForm(), 'success_message': success_message})
    else:
        form = FoodWasteForm()
    return render(request, 'basic_form.html', {'form': form})

@transaction.atomic
def options(request):
    if request.method == 'POST':
        form = FoodOptionsForm(request.POST)
        if form.is_valid():
            form.save()
            # Render a success message
            success_message = "Food Options added successfully!"
            return render(request, 'basic_form.html', {'form': FoodOptionsForm(), 'success_message': success_message})
    else:
        form = FoodOptionsForm()
    return render(request, 'basic_form.html', {'form': form})

@transaction.atomic
def student(request):
    if request.method == 'POST':
        form = FoodPreferenceForm(request.POST)
        if form.is_valid():
            form.save()
            # Render a success message
            success_message = "Food preferences added successfully!"
            return render(request, 'basic_form.html', {'form': FoodPreferenceForm(), 'success_message': success_message})
    else:
        form = FoodPreferenceForm()
    return render(request, 'basic_form.html', {'form': form})

def reports(request):
    if request.method == 'POST':
        form = FoodSpecificReportForm(request.POST)
        if form.is_valid():
            food_name = form.cleaned_data['food_name']
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']

            # Query to get the number of students who prefer the food
            preference_count = FoodPreference.objects.filter(favorite_food=food_name).count()

            # Query to get the total waste produced for the specified food, month, and year
            waste_amount = FoodWaste.objects.filter(food=food_name, date_served__month=month, date_served__year=year).aggregate(Sum('waste_amount'))['waste_amount__sum']

            return render(request, 'report.html', {'food_name': food_name, 'preference_count': preference_count, 'waste_amount': waste_amount, 'form': form})
    else:
        form = FoodSpecificReportForm()

    return render(request, 'generate_report.html', {'form': form})

def generate_waste_report(request):
    if request.method == 'POST':
        form = GeneralReportForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            min_waste = form.cleaned_data.get('min_waste')
            max_waste = form.cleaned_data.get('max_waste')
            min_waste = int(min_waste) if min_waste else None
            max_waste = int(max_waste) if max_waste else None

            # Query all food options and their waste amounts for the selected month
            food_options = FoodOption.objects.all()
            waste_data = []
            for food_option in food_options:
                # Query waste amount for the selected month
                waste_amount = FoodWaste.objects.filter(food=food_option, date_served__month=month, date_served__year=year).aggregate(Sum('waste_amount'))['waste_amount__sum']
                waste_amount = waste_amount or 0
                # Query number of people who prefer the food
                preference_count = FoodPreference.objects.filter(favorite_food=food_option).count()
                if min_waste is not None and max_waste is not None:
                    if min_waste <= waste_amount <= max_waste:
                        waste_data.append({'food_option': food_option, 'waste_amount': waste_amount, 'preference_count': preference_count})
                else:
                    waste_data.append({'food_option': food_option, 'waste_amount': waste_amount, 'preference_count': preference_count})
            return render(request, 'general_report.html', {'form': form, 'waste_data': waste_data})
    else:
        form = GeneralReportForm()
    return render(request, 'generate_general_report.html', {'form': form})

def main_page(request):
    return render(request, 'main_page.html')


