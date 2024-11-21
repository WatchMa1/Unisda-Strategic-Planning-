from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import (
    MainActivity, Report, StrategicTheme, StrategicObjective, Designation, KPI,
    Activity, Achievement, User, Role
)
from .forms import (AchievementForm, ActivityForm, KPIForm, LoginForm, MainActivityForm, StrategicObjectiveForm, StrategicThemeForm, ReportForm, UserForm, RoleForm, DesignationForm, )
from django.views.generic import TemplateView

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class RoleAndDesignationRequiredMixin(LoginRequiredMixin):
    required_role = None  # Set the required role in the view
    required_designation = None  # Set the required designation in the view

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is authenticated (handled by LoginRequiredMixin)
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # Check for the required role
        if self.required_role and (not request.user.role or request.user.role.name != self.required_role):
            raise PermissionDenied("You do not have the required role to access this page.")

        # Check for the required designation
        if self.required_designation and (
            not request.user.designation or request.user.designation.name != self.required_designation
        ):
            raise PermissionDenied("You do not have the required designation to access this page.")

        return super().dispatch(request, *args, **kwargs)


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


class StrategicObjectiveCreateView(RoleAndDesignationRequiredMixin, TemplateView):
    model = StrategicObjective
    required_designation = 'Technical'
    form_class = StrategicObjectiveForm
    template_name = 'forms.html'
    success_url = reverse_lazy('strategic_objective_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'strategic_objective_create'  # Set this for conditional rendering
        return context

class StrategicObjectiveUpdateView(UpdateView):
    model = StrategicObjective
    form_class = StrategicObjectiveForm
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


class DesignationDeleteView(DeleteView):
    model = Designation
    template_name = 'designation_confirm_delete.html'
    success_url = reverse_lazy('designation_list')

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

class MainActivityCreateView(CreateView):
    model = MainActivity
    form_class = MainActivityForm
    template_name = 'planning.html'
    success_url = reverse_lazy('activities')  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'main_activity_create'  # Set this for conditional rendering
        return context
    
    
class MainActivityUpdateView(UpdateView):
    model = MainActivity
    form_class = MainActivityForm
    template_name = 'planning.html'
    success_url = reverse_lazy('activities')  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'main_activity_update'  # Set this for conditional rendering
        return context
    
    
    
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
    form_class = ActivityForm
    template_name = 'forms.html'
    success_url = reverse_lazy('activity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'activity_create'  # Set this for conditional rendering
        return context
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set the logged-in user
        return super().form_valid(form)
    

class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'forms.html'
    success_url = reverse_lazy('activity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'activity_update'  # Set this for conditional rendering
        return context
    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set the logged-in user
        return super().form_valid(form)
    

class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activity_confirm_delete.html'
    success_url = reverse_lazy('activity_list')



# Activity Views
class AchievementListView(ListView):
    model = Achievement
    template_name = 'achievements.html'
    context_object_name = 'activities'


class AchievementDetailView(DetailView):
    model = Achievement
    template_name = 'Achievement_detail.html'
    context_object_name = 'Achievement'


class AchievementCreateView(CreateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'forms.html'
    success_url = reverse_lazy('achievement_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'achievement_create'  # Set this for conditional rendering
        return context

class AchievementUpdateView(UpdateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'forms.html'
    success_url = reverse_lazy('achievement_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'achievement_update'  # Set this for conditional rendering
        return context

class AchievementDeleteView(DeleteView):
    model = Achievement
    template_name = 'Achievement_confirm_delete.html'
    success_url = reverse_lazy('Achievement_list')
    
class DesignationListView(ListView):
    model = Designation
    template_name = 'designations.html'
    context_object_name = 'designations'


class DesignationDetailView(DetailView):
    model = Designation
    template_name = 'designation_detail.html'
    context_object_name = 'designation'


class DesignationCreateView(CreateView):
    model = Designation
    form_class = DesignationForm
    template_name = 'forms.html'
    success_url = reverse_lazy('designation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'designation_create'  # Set this for conditional rendering
        return context


class DesignationUpdateView(UpdateView):
    model = Designation
    form_class = DesignationForm
    template_name = 'forms.html'
    success_url = reverse_lazy('designation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'designation_update'  # Set this for conditional rendering
        return context

class ReportListView(ListView):
    model = Report
    template_name = 'reports.html'
    context_object_name = 'reports'


class ReportDetailView(DetailView):
    model = Report
    template_name = 'report_detail.html'
    context_object_name = 'report'


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'forms.html'
    success_url = reverse_lazy('report_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'report_create'  # Set this for conditional rendering
        return context


class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'forms.html'
    success_url = reverse_lazy('report_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'report_update'  # Set this for conditional rendering
        return context

class RoleListView(ListView):
    model = Role
    template_name = 'roles.html'
    context_object_name = 'roles'


class RoleDetailView(DetailView):
    model = Role
    template_name = 'role_detail.html'
    context_object_name = 'role'


class RoleCreateView(RoleAndDesignationRequiredMixin, TemplateView):
    model = Role
    required_designation = "Technical"
    form_class = RoleForm
    template_name = 'forms.html'
    success_url = reverse_lazy('role_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'role_create'  # Set this for conditional rendering
        return context

class RoleUpdateView(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'forms.html'
    success_url = reverse_lazy('role_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'role_update'  # Set this for conditional rendering
        return context

class UserListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'  # Pass the users to the template


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'forms.html'
    success_url = reverse_lazy('user_list')  # Redirect to the user list after creation
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'user_create'  # Set this for conditional rendering
        return context
    
    def form_valid(self, form):
        """
        Hash the password before saving the user.
        """
        user = form.save(commit=False)
        if user.password:  # Hash password before saving
            user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'forms.html'
    success_url = reverse_lazy('user_list')  # Redirect to the user list after update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'user_update'  # Set this for conditional rendering
        return context
    
    def form_valid(self, form):
        """
        Hash the password before saving the user.
        """
        user = form.save(commit=False)
        if user.password:  # Hash password before saving
            user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data["username"]  # This now represents email
            password = form.cleaned_data["password"]
            print(f"Trying to authenticate user with email: {username}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Authentication successful!")
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Please correct the errors below.")
        return render(request, self.template_name, {"form": form})

def permission_denied(request, exception=None):
    return render(request, "403.html", status=403)

def dashboard(request):
    roles = request.user.groups.values_list('name', flat=True) if request.user.groups.exists() else []
    context = {
        'roles': roles
    }
    return render(request, 'home.html', context)