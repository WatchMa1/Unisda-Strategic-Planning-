from datetime import datetime 
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import (
    MainActivity, Report, StrategicTheme, StrategicObjective, Designation, KPI,
    Activity, User, Role
)
from .forms import ( ActivityForm, KPIForm, LoginForm, MainActivityForm, StrategicObjectiveForm, StrategicThemeForm, ReportForm, UserForm, RoleForm, DesignationForm, )
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from collections import defaultdict

from django.http import FileResponse
from strategic_planning.utils.pdf_generator import generate_pdf
# Create your views here.

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

class HomeView(RoleAndDesignationRequiredMixin, View):
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
    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set the logged-in user
        return super().form_valid(form)

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


class StrategicObjectiveCreateView(RoleAndDesignationRequiredMixin, CreateView):
    model = StrategicObjective
    required_role = 'Admin'
    form_class = StrategicObjectiveForm
    template_name = 'forms.html'
    success_url = reverse_lazy('strategic_objectives')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'strategic_objective_create'  # Set this for conditional rendering
        return context
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set the logged-in user
        return super().form_valid(form)

class StrategicObjectiveUpdateView(UpdateView):
    model = StrategicObjective
    form_class = StrategicObjectiveForm
    template_name = 'forms.html'
    success_url = reverse_lazy('strategic_objectives')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'strategic_objective_update'  # Set this for conditional rendering
        return context
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        return super().form_valid(form)

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
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set the logged-in user
        return super().form_valid(form)


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


class ReportDetailView(DetailView):
    model = Report
    template_name = 'report_detail.html'
    context_object_name = 'report'



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


class RoleCreateView(RoleAndDesignationRequiredMixin, CreateView):
    model = Role
    required_role = "Admin"
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


# Planning Module

class StrategicThemePlanningListView(ListView):
    model = StrategicTheme
    template_name = 'general/base.html'  # Replace with your template name
    context_object_name = 'themes'

    def get_queryset(self):
        # Fetch all strategic themes
        return StrategicTheme.objects.all()


class StrategicObjectivePlanningListView(ListView):
    model = StrategicObjective
    template_name = 'planning.html'  
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme_id = self.kwargs.get('theme_id')
        # Retrieve the StrategicTheme object based on the theme_id
        theme = get_object_or_404(StrategicTheme, id=theme_id) 
        context['theme'] = theme
        context['strategic_objectives'] = self.get_queryset() 
        context['page_name'] = 'objective_planning_list'  
        return context
    
    def get_queryset(self):
        user_designation = self.request.user.designation
        theme_id = self.kwargs.get('theme_id')
        queryset = StrategicObjective.objects.filter(
        strategic_theme__id=theme_id,
        designation=user_designation
        )

        return queryset
    
class KPIPlanningListView(ListView):
    model = KPI
    template_name = 'planning.html'  # Replace with your template name
    context_object_name = 'kpis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        strategic_objective_id = self.kwargs.get('strategic_objective_id')

        # Retrieve the strategic objective
        objective = get_object_or_404(StrategicObjective, id=strategic_objective_id)
        context['objective'] = objective
        context['page_name'] = 'kpi_planning_list'
        return context

    def get_queryset(self):
        objective_id = self.kwargs.get('strategic_objective_id')
        queryset = KPI.objects.filter(strategic_objective_id=objective_id)
        return queryset


def main_activity_create(request, kpi_id):
    kpi = get_object_or_404(KPI, id=kpi_id)
    form = MainActivityForm()  # Your form logic here

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'partials/kpi_content.html', {'form': form, 'kpi': kpi})

    return render(request, 'full_template.html', {'form': form, 'kpi': kpi})

class MainActivityCreateView(CreateView):
    model = MainActivity
    form_class = MainActivityForm
    template_name = 'planning.html'
    success_url = reverse_lazy('activities')  # Replace with your success URL
    
    def form_valid(self, form):
        """
        Set the KPI field to the KPI object based on kpi_id before saving.
        """
        kpi_id = self.kwargs.get('kpi_id')
        form.instance.kpi = get_object_or_404(KPI, id=kpi_id)
        form.instance.created_by = self.request.user  # Optionally set the creator
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kpi_id = self.kwargs.get('kpi_id')
        name = get_object_or_404(KPI, id=kpi_id)
        context['kpi'] = name
        context['page_name'] = 'main_activity_create'  # Set this for conditional rendering
        return context
    
    def get_success_url(self):
        # Redirect to SubActivityCreate view after submitting
        main_activity_id = self.object.id
        kpi_id = self.kwargs.get('kpi_id')
        if self.object and main_activity_id:
            return reverse_lazy('sub_activity_create', kwargs={
                'kpi_id': kpi_id,
                'main_activity_id': main_activity_id
            })
        else:
            return reverse_lazy('sub_activity_create_without_main', kwargs={
                'kpi_id': kpi_id
        })
    
class MainActivityUpdateView(UpdateView):
    model = MainActivity
    form_class = MainActivityForm
    template_name = 'planning.html'
    success_url = reverse_lazy('activities')  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'main_activity_update'  # Set this for conditional rendering
        return context
class ActivityPlanningUpdateView(UpdateView):
    model = MainActivity
    form_class = MainActivityForm
    template_name = 'planning.html'
    success_url = reverse_lazy('activities')  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'sub_activity_update'  # Set this for conditional rendering
        return context
    
class ActivityPlanningCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'planning.html'
    success_url = reverse_lazy('sub_activity_create')  # Replace with your success URL
    
    def form_valid(self, form):
        """
        Set the KPI field to the KPI object based on kpi_id before saving.
        """
        kpi_id = self.kwargs.get('kpi_id')
        main_activity_id = self.kwargs.get('main_activity_id')
        form.instance.kpi = get_object_or_404(KPI, id=kpi_id)
        if main_activity_id:
            form.instance.main_activity = get_object_or_404(MainActivity, id=main_activity_id)
        
        form.instance.created_by = self.request.user  # Optionally set the creator
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kpi_id = self.kwargs.get('kpi_id')
        
        name = get_object_or_404(KPI, id=kpi_id)
        context['kpi'] = name
        context['page_name'] = 'sub_activity_create'  # Set this for conditional rendering
        return context
    def get_success_url(self):
        # Redirect to SubActivityCreate view after submitting
        main_activity_id = self.kwargs.get('main_activity_id')
        kpi_id = self.kwargs.get('kpi_id')
        if self.object and main_activity_id:
            return reverse_lazy('sub_activity_create', kwargs={
                'kpi_id': kpi_id,
                'main_activity_id': main_activity_id
            })
        else:
            return reverse_lazy('sub_activity_create_without_main', kwargs={
                'kpi_id': kpi_id
        })
            
            
class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports.html'
    success_url = reverse_lazy('report_list')  # Replace with your actual report list URL name

    def form_valid(self, form):
        # Automatically set the user and designation from the logged-in user
        form.instance.user = self.request.user
        form.instance.designation = self.request.user.designation  # Assuming `designation` is a field in the User model
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kpi_id = self.kwargs.get('kpi_id')
        
        
        context['page_name'] = 'main_activity_create'  # Set this for conditional rendering
        return context
    
class ReportListView(TemplateView):
    template_name = 'reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get activities and reports
        activities = Activity.objects.all()
        reports = Report.objects.filter(designation=self.request.user.designation)

        # Create a mapping of activity IDs to their reports
        reports_by_activity = {report.activity_id: report for report in reports}

        # Pass activities, reports, and the form to the context
        context['activities'] = activities
        context['reports_by_activity'] = reports_by_activity  # Pre-filtered reports by activity ID
        context['form'] = ReportForm()
        return context
    
class ActivityReportView(TemplateView):
    template_name = 'report_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = Activity.objects.all()  # Fetch all activities
        context['reports'] = Report.objects.filter(designation=self.request.user.designation)
        context['form'] = ReportForm()
        return context

class SubmitReportView(View):
    def post(self, request, activity_id):
        # Fetch the activity object
        activity = get_object_or_404(Activity, id=activity_id)

        # Get or create the report object for the user and activity
        report, created = Report.objects.get_or_create(
            user=request.user,
            activity=activity,
            defaults={'designation': request.user.designation}
        )

        if report.status == 1:
            messages.error(request, "This report has already been submitted.")
            return redirect('report_list')  

        # Bind the form to the POST data
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.instance.designation = self.request.user.designation
            form.save()
            report.status = 1  # Mark report as submitted
            report.save()
            messages.success(request, "Report submitted successfully.")
        else:
            messages.error(request, "There was an error submitting the report.")

        # Redirect back to the report list page
        return redirect('report_list') 

class FullReportView(TemplateView):
    template_name = "reports_templates/full-reports.html"  # The HTML template for the table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the logged-in user 
        user = self.request.user
        quarter = ''
        current_month = datetime.now().month

        # Determine the quarter based on the current month
        if 1 <= current_month <= 3:
            quarter = "First"
        elif 4 <= current_month <= 6:
            quarter = "Second"
        elif 7 <= current_month <= 9:
            quarter = "Third"
        elif 10 <= current_month <= 12:
            quarter = "Fourth"
            
        context["request"] = self.request.user.designation.name
        context["user"] = self.request.user
        context["quarter"] = quarter
        # Fetch all themes
        themes = StrategicTheme.objects.all()

        # Create structured data for the table
        data = []
        for theme in themes:
            objectives = theme.objectives.all()
            for objective in objectives:
                kpis = objective.kpis.all()
                for kpi in kpis:
                    main_activities = kpi.main_activities.all()
                    for main_activity in main_activities:
                        activities = main_activity.activities.all()
                        for activity in activities:
                            # Fetch the report if available
                            report = activity.reports.filter(user=user).first()

                            data.append({
                                "theme": theme.theme_name,
                                "objective": objective.objective_name,
                                "kpi": kpi.name,
                                "main_activity": main_activity.name,
                                "activity": activity.name,
                                "status": report.goal_score if report else "No Report",
                                "q1": "",  # Leave empty for now
                                "report_details": report.report_details if report else "No details",
                            })

        context["data"] = data
        return context
class DepartmentalReportView(TemplateView):
    template_name = "reports_templates/departmental-reports.html"  # The HTML template for the table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the logged-in user 
        user = self.request.user
        quarter=''
        current_month = datetime.now().month

        # Determine the quarter based on the current month
        if 1 <= current_month <= 3:
            quarter = "First"
        elif 4 <= current_month <= 6:
            quarter = "Second"
        elif 7 <= current_month <= 9:
            quarter = "Third"
        elif 10 <= current_month <= 12:
            quarter = "Fourth"
            
        context["request"] = self.request.user.designation.name
        context["user"] = self.request.user
        context["quarter"] = quarter
        # Fetch all themes
        themes = StrategicTheme.objects.all()

        # Create structured data for the table
        data = []
        for theme in themes:
            objectives = theme.objectives.filter(designation__users=user)
            for objective in objectives:
                kpis = objective.kpis.all()
                for kpi in kpis:
                    main_activities = kpi.main_activities.all()
                    for main_activity in main_activities:
                        activities = main_activity.activities.all()
                        for activity in activities:
                            # Fetch the report if available
                            report = activity.reports.filter(user=user).first()
                            
                            

                            data.append({
                                "theme": theme.theme_name,
                                "objective": objective.objective_name,
                                "kpi": kpi.name,
                                "main_activity": main_activity.name,
                                "activity": activity.name,
                                "status": report.goal_score if report else "No Report",
                                "q1": "",  # Leave empty for now
                                "report_details": report.report_details if report else "No details",
                            })

        context["data"] = data
        return context


class AdminReportsListView(ListView):
    model = Designation
    template_name = 'admin-reports.html'  # Update with actual template path
    context_object_name = 'designations'
    
class AdminReportsListView(ListView):
    model = Designation
    template_name = 'admin-reports.html'  
    def get_queryset(self):
        queryset = Designation.objects.all()
        return queryset
class AdminReportListView(TemplateView):
    template_name = 'reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get activities and reports
        activities = Activity.objects.all()
        reports = Report.objects.filter(designation=self.request.user.designation)

        # Create a mapping of activity IDs to their reports
        reports_by_activity = {report.activity_id: report for report in reports}

        # Pass activities, reports, and the form to the context
        context['activities'] = activities
        context['reports_by_activity'] = reports_by_activity  # Pre-filtered reports by activity ID
        context['form'] = ReportForm()
        return context
    
    
def download_pdf(request):
    themes = StrategicTheme.objects.prefetch_related(
        'objectives__kpis__main_activities__activities'
    ).all()

    data = []
    for theme in themes:
        theme_row_span = 0
        objectives_data = []
        for obj in theme.objectives.all():
            objective_row_span = 0
            kpis_data = []
            for kpi in obj.kpis.all():
                kpi_row_span = kpi.main_activities.count() or 1
                main_activities_data = [
                    {
                        "main_activity": ma,
                        "activities": ma.activities.all()
                    } for ma in kpi.main_activities.all()
                ]
                kpis_data.append({
                    "kpi": kpi,
                    "kpi_row_span": kpi_row_span,
                    "main_activities": main_activities_data,
                })
                objective_row_span += kpi_row_span
            objectives_data.append({
                "objective": obj,
                "objective_row_span": objective_row_span,
                "kpis": kpis_data,
            })
            theme_row_span += objective_row_span
        data.append({
            "theme": theme,
            "theme_row_span": theme_row_span,
            "objectives": objectives_data,
        })
    
    # Generate the PDF
    pdf_filename = "strategic_themes.pdf"
    generate_pdf(data, pdf_filename)
    return FileResponse(open(pdf_filename, 'rb'), as_attachment=True, filename=pdf_filename)
