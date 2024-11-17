from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    StrategicTheme, StrategicObjective, Department, KPI,
    Activity, Budget, Achievement, User, Role
)
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class StrategicThemeListView(ListView):
    model = StrategicTheme
    template_name = 'strategic_theme_list.html'
    context_object_name = 'strategic_themes'


class StrategicThemeDetailView(DetailView):
    model = StrategicTheme
    template_name = 'strategic_theme_detail.html'
    context_object_name = 'strategic_theme'


class StrategicThemeCreateView(CreateView):
    model = StrategicTheme
    fields = ['theme_name', 'created_by']
    template_name = 'strategic_theme_form.html'
    success_url = reverse_lazy('strategic_theme_list')


class StrategicThemeUpdateView(UpdateView):
    model = StrategicTheme
    fields = ['theme_name', 'created_by']
    template_name = 'strategic_theme_form.html'
    success_url = reverse_lazy('strategic_theme_list')


class StrategicThemeDeleteView(DeleteView):
    model = StrategicTheme
    template_name = 'strategic_theme_confirm_delete.html'
    success_url = reverse_lazy('strategic_theme_list')


#strategic objectives views 
class StrategicObjectiveListView(ListView):
    model = StrategicObjective
    template_name = 'strategic_objective_list.html'
    context_object_name = 'strategic_objectives'


class StrategicObjectiveDetailView(DetailView):
    model = StrategicObjective
    template_name = 'strategic_objective_detail.html'
    context_object_name = 'strategic_objective'


class StrategicObjectiveCreateView(CreateView):
    model = StrategicObjective
    fields = ['objective_name', 'created_by', 'theme', 'department']
    template_name = 'strategic_objective_form.html'
    success_url = reverse_lazy('strategic_objective_list')


class StrategicObjectiveUpdateView(UpdateView):
    model = StrategicObjective
    fields = ['objective_name', 'created_by', 'theme', 'department']
    template_name = 'strategic_objective_form.html'
    success_url = reverse_lazy('strategic_objective_list')


class StrategicObjectiveDeleteView(DeleteView):
    model = StrategicObjective
    template_name = 'strategic_objective_confirm_delete.html'
    success_url = reverse_lazy('strategic_objective_list')

# Department Views
class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    fields = ['name', 'created_by']
    template_name = 'department_form.html'
    success_url = reverse_lazy('department_list')


class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['name', 'created_by']
    template_name = 'department_form.html'
    success_url = reverse_lazy('department_list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department_confirm_delete.html'
    success_url = reverse_lazy('department_list')

#KPI Views
class KPIListView(ListView):
    model = KPI
    template_name = 'kpi_list.html'
    context_object_name = 'kpis'


class KPIDetailView(DetailView):
    model = KPI
    template_name = 'kpi_detail.html'
    context_object_name = 'kpi'


class KPICreateView(CreateView):
    model = KPI
    fields = ['name', 'objective']
    template_name = 'kpi_form.html'
    success_url = reverse_lazy('kpi_list')


class KPIUpdateView(UpdateView):
    model = KPI
    fields = ['name', 'objective']
    template_name = 'kpi_form.html'
    success_url = reverse_lazy('kpi_list')


class KPIDeleteView(DeleteView):
    model = KPI
    template_name = 'kpi_confirm_delete.html'
    success_url = reverse_lazy('kpi_list')


# Activity Views
class ActivityListView(ListView):
    model = Activity
    template_name = 'activity_list.html'
    context_object_name = 'activities'


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'
    context_object_name = 'activity'


class ActivityCreateView(CreateView):
    model = Activity
    fields = ['name', 'objective', 'parent_activity']
    template_name = 'activity_form.html'
    success_url = reverse_lazy('activity_list')


class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ['name', 'objective', 'parent_activity']
    template_name = 'activity_form.html'
    success_url = reverse_lazy('activity_list')


class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activity_confirm_delete.html'
    success_url = reverse_lazy('activity_list')
