from django.urls import path

import apps.main.views as view

app_name='main'

urlpatterns = [
    path('',view.index),
    
]
