from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.image_to_text, name='image_to_text'),
    path('box/', views.image_to_boxes, name='image_to_boxes'),
    path('data/', views.image_to_data, name='image_to_data'),
]