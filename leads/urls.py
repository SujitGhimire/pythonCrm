from django.urls import URLPattern, path
from .views import  lead_list

app_name='leads'
urlpatterns = [
    path('',lead_list)
]
