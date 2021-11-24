from django.urls import path
from .views import *
urlpatterns=[
    path('add/',AddLaptopView.as_view(),name='add'),
    path('display/',DisplayLaptopView.as_view(),name='display'),
    path('<pk>/update',UpdateLaptopView.as_view(),name='updt'),
    path('<pk>/delete',DeleteLaptopView.as_view(),name='dlt'),
]