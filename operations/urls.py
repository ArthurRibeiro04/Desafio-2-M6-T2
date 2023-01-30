from django.urls import path
from .views import OperationsView

urlpatterns = [
    path('operations/', OperationsView.as_view()),
]