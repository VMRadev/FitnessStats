from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from AutoHeaven.accounts.forms import AccountCreationForm, ProfileEditForm, CustomLoginForm
from AutoHeaven.accounts.models import Profile

UserModel = get_user_model()


# Create your views here.
class AccountCreateView(CreateView):
    form_class = AccountCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form = super().form_valid(form)

        # login(self.request, self.object)

        return form

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'registration/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = context['profile'].user

        return context

class CustomLoginView(LoginView):
    form_class = CustomLoginForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'registration/profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    success_url = reverse_lazy('index')
    template_name = 'registration/profile-delete.html'

    def get_object(self, queryset=None):
        return UserModel.objects.get(pk=self.request.user.pk)