from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from FitnessStats.accounts.views import AccountCreateView, ProfileDetailView, ProfileUpdateView, AccountDeleteView

urlpatterns = [
    path('register/', AccountCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', ProfileUpdateView.as_view(), name='profile-update'),
    path('delete/', AccountDeleteView.as_view(), name='profile-delete'),
]