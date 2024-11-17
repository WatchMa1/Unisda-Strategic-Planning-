from django import forms
from .models import (
    User, Department, StrategicTheme, StrategicObjective, KPI, 
    Activity, Budget, Achievement, Role, Report
)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'dob', 'contact', 'email', 'physical_address']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'created_by']

class StrategicThemeForm(forms.ModelForm):
    class Meta:
        model = StrategicTheme
        fields = ['theme_name', 'description', 'created_by']

class StrategicObjectiveForm(forms.ModelForm):
    class Meta:
        model = StrategicObjective
        fields = ['objective_name', 'strategic_theme', 'department', 'created_by']

class KPIForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = ['name', 'strategic_objective', 'created_by']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'kpi', 'parent_activity', 'created_by']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['estimated_amount', 'actual_amount', 'activity']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['goal_score', 'color_code', 'explanation', 'activity']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['user', 'department', 'role_name']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['quarter', 'user', 'department', 'activity', 'report_details']
