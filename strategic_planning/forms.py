from django import forms
from .models import (
    User, Department, StrategicTheme, StrategicObjective, KPI, 
    Activity, Achievement, Role, Report
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
        labels = {
            'theme_name': 'Theme Name',
            'description': 'Description',
            'created_by': 'Created By',
        }
        widgets = {
            'theme_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter theme name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
        }

class StrategicObjectiveForm(forms.ModelForm):
    class Meta:
        model = StrategicObjective
        fields = ['objective_name', 'strategic_theme', 'department', 'created_by']
        labels = {
            'objective_name': 'Objective',
            'strategic_theme': 'Strategic Theme',
            'department': 'Department',
            'created_by': 'Created By',
        }
        widgets = {
            'objective_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Objective'}),
            'strategic_theme': forms.Select(attrs={
                'class': 'form-control'
                }),
            'department': forms.Select(attrs={
                'class': 'form-control'
                }),
            'created_by': forms.Select(attrs={
                'class': 'form-control'
                }),
        }



from django import forms
from .models import KPI

class KPIForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = ['name', 'strategic_objective', 'created_by']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter KPI Name'
            }),
            'strategic_objective': forms.Select(attrs={
                'class': 'form-control',
            }),
            'created_by': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'name': 'KPI Name',
            'strategic_objective': 'Strategic Objective',
            'created_by': 'Created By',
        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            'name', 'description', 'kpi', 'parent_activity', 
            'estimated_amount', 'actual_amount', 'created_by'
        ]
        labels = {
            'name': 'Activity Name',
            'description': 'Activity Description',
            'kpi': 'Associated KPI',
            'parent_activity': 'Parent Activity (if any)',
            'estimated_amount': 'Estimated Budget Amount',
            'actual_amount': 'Actual Amount (Optional)',
            'created_by': 'Created By',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the activity name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter activity details',
                'rows': 4,
            }),
            'kpi': forms.Select(attrs={
                'class': 'form-control',
            }),
            'parent_activity': forms.Select(attrs={
                'class': 'form-control',
            }),
            'estimated_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the estimated budget',
            }),
            'actual_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the actual amount spent (if applicable)',
            }),
            'created_by': forms.TextInput(attrs={
                'class': 'form-control'
                
            }),
        }


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
