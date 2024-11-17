from django.urls import path
from . import views
from .views import (
    HomeView,StrategicThemeListView, StrategicThemeDetailView, StrategicThemeCreateView, StrategicThemeUpdateView, StrategicThemeDeleteView,
    StrategicObjectiveListView, StrategicObjectiveDetailView, StrategicObjectiveCreateView, StrategicObjectiveUpdateView, StrategicObjectiveDeleteView,
    DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView,
    KPIListView, KPIDetailView, KPICreateView, KPIUpdateView, KPIDeleteView,
    ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('strategic-themes/', StrategicThemeListView.as_view(), name='strategic_themes'),
    path('strategic-themes/<int:pk>/', StrategicThemeDetailView.as_view(), name='strategic_theme_detail'),
    path('strategic-themes/create/', StrategicThemeCreateView.as_view(), name='strategic_theme_create'),
    path('strategic-themes/<int:pk>/update/', StrategicThemeUpdateView.as_view(), name='strategic_theme_update'),
    path('strategic-themes/<int:pk>/delete/', StrategicThemeDeleteView.as_view(), name='strategic_theme_delete'),
    
    path('strategic-objectives/', StrategicObjectiveListView.as_view(), name='strategic_objectives'),
    path('strategic-objectives/<int:pk>/', StrategicObjectiveDetailView.as_view(), name='strategic_objective_detail'),
    path('strategic-objectives/create/', StrategicObjectiveCreateView.as_view(), name='strategic_objective_create'),
    path('strategic-objectives/<int:pk>/update/', StrategicObjectiveUpdateView.as_view(), name='strategic_objective_update'),
    path('strategic-objectives/<int:pk>/delete/', StrategicObjectiveDeleteView.as_view(), name='strategic_objective_delete'),
    
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),
    
    path('kpis/', KPIListView.as_view(), name='kpi_list'),
    path('kpis/<int:pk>/', KPIDetailView.as_view(), name='kpi_detail'),
    path('kpis/create/', KPICreateView.as_view(), name='kpi_create'),
    path('kpis/<int:pk>/update/', KPIUpdateView.as_view(), name='kpi_update'),
    path('kpis/<int:pk>/delete/', KPIDeleteView.as_view(), name='kpi_delete'),
    
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
    path('activities/create/', ActivityCreateView.as_view(), name='activity_create'),
    path('activities/<int:pk>/update/', ActivityUpdateView.as_view(), name='activity_update'),
    path('activities/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity_delete'),
]
