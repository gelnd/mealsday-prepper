from django.urls import path
from .views import DefaultView

urlpatterns = [
    path('default/', DefaultView.as_view(), name='default')
]
