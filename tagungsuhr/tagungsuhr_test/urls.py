from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default app. Run index-function which is one of my views
    path('tagungsuhr_test/', views.tagungsuhr_test),
    path('extra/', views.extra)
]