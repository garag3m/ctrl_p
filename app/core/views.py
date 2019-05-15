# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models

from django.contrib.auth.decorators import login_required #new
from django.utils.decorators import method_decorator #new

# Dashboard
# https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#templateview
# - - - - - - - - - - - - - - - - - - -

@method_decorator(login_required(login_url='/'), name='dispatch') #new
class DashboardView(TemplateView):

    template_name = 'core/dashboard.html'


# Users list view
# - - - - - - - - - - - - - - - - - - -
@method_decorator(login_required(login_url='/'), name='dispatch') #new
class UsersView(ListView):

    model = models.UUIDUser
    template_name = 'core/user/list.html'


# User create
# - - - - - - - - - - - - - - - - - - -
@method_decorator(login_required(login_url='/'), name='dispatch') #new
class UserCreateView(CreateView):

    model = models.UUIDUser
    template_name = 'core/user/form.html'
    success_url = reverse_lazy('core:users-list')
    fields = ['username','first_name', 'last_name', 'password', 'email', 'cpf', 'registration', 'picture']

    #Recebe usuário do formulário seleciona a senha criptografa e salva a senha
    def form_valid(self, form): #new
        self.object = form.save(commit=False)
        # things
        self.object.set_password(self.object.password)
        self.object.save()


        return http.HttpResponseRedirect(self.get_success_url())


# User edit
# - - - - - - - - - - - - - - - - - - -
@method_decorator(login_required(login_url='/'), name='dispatch') #new
class UserEditView(UpdateView):

    model = models.UUIDUser
    template_name = 'core/user/update.html'
    success_url = reverse_lazy('core:users-list')
    fields = ['username','first_name', 'last_name', 'password', 'email', 'cpf', 'registration', 'picture']