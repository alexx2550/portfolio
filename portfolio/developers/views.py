from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Programmer, Project

class ProgrammerListView(ListView):
    model = Programmer
    template_name = 'developers/programmer_list.html'
    context_object_name = 'programmers'

class ProgrammerDetailView(DetailView):
    model = Programmer
    template_name = 'developers/programmer_detail.html'
    context_object_name = 'programmer'

class ProgrammerCreateView(LoginRequiredMixin, CreateView):
    model = Programmer
    template_name = 'developers/add_programmer.html'
    fields = ['user', 'age', 'language', 'framework', 'experience']
    success_url = reverse_lazy('programmer_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'developers/add_project.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.programmer = Programmer.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
