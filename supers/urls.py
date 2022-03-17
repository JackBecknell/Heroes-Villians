from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.SupersList.as_view()),
    path('<int:pk>/', views.SupersDetail.as_view())
    #will add another path for <int:pk> once the class is built
]