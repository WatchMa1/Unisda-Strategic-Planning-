from django.db import models
from django.utils.timezone import now
# ENUM Choices
class QuaterEnum(models.TextChoices):
    FIRST = '1st', '1st'
    SECOND = '2nd', '2nd'
    THIRD = '3rd', '3rd'
    FOURTH = '4th', '4th'

class ColorCodeEnum(models.TextChoices):
    GREEN = 'green', 'Green'
    ORANGE = 'orange', 'Orange'
    YELLOW = 'yellow', 'Yellow'
    RED = 'red', 'Red'

class GoalScoreEnum(models.TextChoices):
    FULL = '100', '100'
    HIGH = '50-99', '50-99'
    MEDIUM = '1-49', '1-49'
    LOW = '0', '0'

# Models
class User(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    physical_address = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StrategicTheme(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    theme_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.theme_name

class StrategicObjective(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    objective_name = models.CharField(max_length=200)
    strategic_theme = models.ForeignKey(StrategicTheme, on_delete=models.CASCADE, related_name="objectives")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="objectives")
    
    def __str__(self):
        return self.objective_name

class KPI(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    strategic_objective = models.ForeignKey(StrategicObjective, on_delete=models.CASCADE, related_name="kpis")

    def __str__(self):
        return self.name

class Activity(models.Model):
    date_created = models.DateTimeField(default=now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, related_name="activities")
    parent_activity = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="sub_activities")
    estimated_amount = models.DecimalField(max_digits=12, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Achievement(models.Model):
    goal_score = models.CharField(max_length=10, choices=GoalScoreEnum.choices)
    color_code = models.CharField(max_length=10, choices=ColorCodeEnum.choices)
    explanation = models.TextField()
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE, related_name="achievement")

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="roles")
    role_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.name} - {self.role_name}"

class Report(models.Model):
    quarter = models.CharField(max_length=10, choices=QuaterEnum.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="reports")
    report_details = models.TextField()

    def __str__(self):
        return f"Report by {self.user.name} for {self.quarter}"
