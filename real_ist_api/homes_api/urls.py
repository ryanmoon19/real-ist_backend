from django.urls import path 
from . import views 

urlpatterns = [
    path('homes', views.HomeList.as_view(), name='home_list'),
    path('homes/<int:pk>', views.HomeDetail.as_view(), name='home_detail'),
]