from django.db import models

# Create your models here.
from django.db import models

class StrategicTheme(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    theme_name = models.CharField(max_length=255)

    def __str__(self):
        return self.theme_name


class Department(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class StrategicObjective(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    objective_name = models.CharField(max_length=255)
    theme = models.ForeignKey(StrategicTheme, on_delete=models.CASCADE, related_name="objectives")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="objectives")

    def __str__(self):
        return self.objective_name


class KPI(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    objective = models.ForeignKey(StrategicObjective, on_delete=models.CASCADE, related_name="kpis")

    def __str__(self):
        return self.name


class Activity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    objective = models.ForeignKey(StrategicObjective, on_delete=models.CASCADE, related_name="activities")
    parent_activity = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="sub_activities")

    def __str__(self):
        return self.name


class Quarter(models.TextChoices):
    FIRST = '1st', '1st'
    SECOND = '2nd', '2nd'
    THIRD = '3rd', '3rd'
    FOURTH = '4th', '4th'


class Budget(models.Model):
    estimated_amount = models.DecimalField(max_digits=15, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=15, decimal_places=2)
    objective = models.ForeignKey(StrategicObjective, on_delete=models.CASCADE, related_name="budgets")
    quarter = models.CharField(max_length=3, choices=Quarter.choices)

    def __str__(self):
        return f"{self.objective.objective_name} - {self.quarter} Budget"


class Achievement(models.Model):
    goal_score = models.FloatField()
    color_code = models.CharField(max_length=7)  # Hex color code
    explanation = models.TextField()
    objective = models.ForeignKey(StrategicObjective, on_delete=models.CASCADE, related_name="achievements")
    quarter = models.CharField(max_length=3, choices=Quarter.choices)

    def __str__(self):
        return f"{self.objective.objective_name} - {self.quarter} Achievement"


class User(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField("Date of Birth")
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    physical_address = models.TextField()

    def __str__(self):
        return self.name


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="roles")
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.name} - {self.role_name}"
