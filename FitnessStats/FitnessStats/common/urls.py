from django.urls import path
from FitnessStats.common.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]