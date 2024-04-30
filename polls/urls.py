from django.urls import path

from . import views

urlpatterns = [
		path("", views.main_page, name='main_page'),
    path("food_specific_report/", views.reports, name="food specific report"),
		path("general_waste_report/", views.generate_waste_report, name = "general waste report"),
		path("waste/", views.waste, name="waste"),
		path("options/", views.options, name="options"),
		path("student/", views.student, name="student")
]
