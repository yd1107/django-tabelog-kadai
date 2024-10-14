from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import forms
from . import models

# Create your views here.
class UserDetailView(generic.DetailView):
    model = models.CustomUser
    template_name = 'user/user_detail.html'
    

class UserUpdateView(generic.UpdateView):
    model = models.CustomUser
    template_name = 'user/user_update.html'
    form_class = forms.UserUpdateForm

    def get_success_url(self):
      pk = self.kwargs['pk']
      return reverse_lazy('user_detail', kwargs={'pk': pk})

    def form_valid(self, form):
      return super().form_valid(form)
      
    def form_invalid(self, form):
      return super().form_invalid(form)