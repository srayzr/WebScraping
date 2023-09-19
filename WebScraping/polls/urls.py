from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.scrape_and_print_jobs, name='scrape_and_print_jobs'),

]
