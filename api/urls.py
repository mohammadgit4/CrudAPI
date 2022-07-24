from django.urls import path
from .views import StudentView

urlpatterns = [
    path('addshow/', StudentView.as_view(), name='showdata'),
    path('rud/<int:pk>/', StudentView.as_view(), name='aud')
]
