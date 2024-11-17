from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    StrategicTheme, StrategicObjective, Department, KPI,
    Activity, Achievement, User, Role
)
from .forms import (KPIForm, StrategicObjectiveForm, StrategicThemeForm)

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class StrategicThemeListView(ListView):
    model = StrategicTheme
    template_name = 'strategic_themes.html'
    context_object_name = 'strategic_themes'

class StrategicThemeCreateView(CreateView):
    model = StrategicTheme
    form_class = StrategicThemeForm
    template_name = 'forms.html'
    success_url = reverse_lazy('strategic_themes')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'strategic_theme_create'  # Set this for conditional rendering
        return context
    
class StrategicThemeDetailView(DetailView):
    model = StrategicTheme
    template_name = 'strategic_theme_detail.html'
    context_object_name = 'strategic_theme'


class StrategicThemeUpdateView(UpdateView):
    model = StrategicTheme
    form_class = StrategicThemeForm
    template_name = 'forms.html'  # Your form template
    success_url = reverse_lazy('strategic_themes')  # Redirect after saving

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'strategic_theme_update'
        return context


class StrategicThemeDeleteView(DeleteView):
    model = StrategicTheme
    template_name = 'strategic_theme_confirm_delete.html'
    success_url = reverse_lazy('strategic_theme_list')


#strategic objectives views 
class StrategicObjectiveListView(ListView):
    model = StrategicObjective
    template_name = 'strategic_objectives.html'
    context_object_name = 'strategic_objectives'


class StrategicObjectiveDetailView(DetailView):
    model = StrategicObjective
    template_name = 'strategic_objective_detail.html'
    context_object_name = 'strategic_objective'


class StrategicObjectiveCreateView(CreateView):
    model = StrategicObjective
    fields = ['objective_name', 'created_by', 'strategic_theme', 'department']
    template_name = 'forms.html'
    success_url = reverse_lazy('strategic_objective_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'strategic_objective_create'  # Set this for conditional rendering
        return context

class StrategicObjectiveUpdateView(UpdateView):
    model = StrategicObjective
    fields = ['objective_name', 'created_by', 'strategic_theme', 'department']
    template_name = 'forms.html'
    success_url = reverse_lazy('strategic_objectives')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'strategic_objective_update'  # Set this for conditional rendering
        return context

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
    form_class = KPIForm
    template_name = 'forms.html'
    success_url = reverse_lazy('kpi_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'kpi_create'  # Set this for conditional rendering
        return context


class KPIUpdateView(UpdateView):
    model = KPI
    form_class = KPIForm
    template_name = 'forms.html'
    success_url = reverse_lazy('kpi_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'kpi_update'  # Set this for conditional rendering
        return context

class KPIDeleteView(DeleteView):
    model = KPI
    template_name = 'kpi_confirm_delete.html'
    success_url = reverse_lazy('kpi_list')


# Activity Views
class ActivityListView(ListView):
    model = Activity
    template_name = 'activities.html'
    context_object_name = 'activities'


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'
    context_object_name = 'activity'


class ActivityCreateView(CreateView):
    model = Activity
    fields = [
            'name', 'description', 'kpi', 'parent_activity', 
            'estimated_amount', 'actual_amount', 'created_by'
        ]
    template_name = 'forms.html'
    success_url = reverse_lazy('activity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'activity_create'  # Set this for conditional rendering
        return context

class ActivityUpdateView(UpdateView):
    model = Activity
    fields = [
            'name', 'description', 'kpi', 'parent_activity', 
            'estimated_amount', 'actual_amount', 'created_by'
        ]
    template_name = 'forms.html'
    success_url = reverse_lazy('activity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'activity_update'  # Set this for conditional rendering
        return context

class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activity_confirm_delete.html'
    success_url = reverse_lazy('activity_list')
