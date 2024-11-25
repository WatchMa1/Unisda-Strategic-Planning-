from django.urls import path
from .views import (
    ActivityPlanningCreateView, ActivityPlanningUpdateView, ActivityReportView, HomeView, KPIPlanningListView, LoginView, MainActivityCreateView, MainActivityUpdateView, ReportCreateView, ReportDetailView, ReportListView, ReportUpdateView, RoleCreateView, RoleDetailView, RoleListView, RoleUpdateView, StrategicObjectivePlanningListView,StrategicThemeListView, StrategicThemeDetailView, StrategicThemeCreateView, StrategicThemePlanningListView, StrategicThemeUpdateView, StrategicThemeDeleteView,
    StrategicObjectiveListView, StrategicObjectiveDetailView, StrategicObjectiveCreateView, StrategicObjectiveUpdateView, StrategicObjectiveDeleteView,
    DesignationListView, DesignationDetailView, DesignationCreateView, DesignationUpdateView, DesignationDeleteView,
    KPIListView, KPIDetailView, KPICreateView, KPIUpdateView, KPIDeleteView,
    ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView, SubmitReportView, UserCreateView, UserListView, UserUpdateView
)

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='user_login'),
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
    
    path('designations/', DesignationListView.as_view(), name='designation_list'),
    path('designations/<int:pk>/', DesignationDetailView.as_view(), name='designation_detail'),
    path('designations/create/', DesignationCreateView.as_view(), name='designation_create'),
    path('designations/<int:pk>/update/', DesignationUpdateView.as_view(), name='designation_update'),
    path('designations/<int:pk>/delete/', DesignationDeleteView.as_view(), name='designation_delete'),
    
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
    
    
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
    path('roles/create/', RoleCreateView.as_view(), name='role_create'),
    path('roles/update/<int:pk>/', RoleUpdateView.as_view(), name='role_update'),

    # Designation URLs
    path('designations/', DesignationListView.as_view(), name='designation_list'),
    path('designations/<int:pk>/', DesignationDetailView.as_view(), name='designation_detail'),
    path('designations/create/', DesignationCreateView.as_view(), name='designation_create'),
    path('designations/update/<int:pk>/', DesignationUpdateView.as_view(), name='designation_update'),

    # Report URLs
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('reports/create/', ReportCreateView.as_view(), name='report_create'),
    path('reports/update/<int:pk>/', ReportUpdateView.as_view(), name='report_update'),
    
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    
    # Planning Views
    path('main-activity/create/<int:kpi_id>/', MainActivityCreateView.as_view(), name='main_activity_create'),
    path('main-activity/update/', MainActivityUpdateView.as_view(), name='main_activity_update'),
    path('sub-activity/create//<int:kpi_id>/<int:main_activity_id>/', ActivityPlanningCreateView.as_view(), name='sub_activity_create'),
    path('sub-activity/create//<int:kpi_id>/', ActivityPlanningCreateView.as_view(), name='sub_activity_create_without_main'),
    path('sub-activity/update/', ActivityPlanningUpdateView.as_view(), name='sub_activity_update'),
    
    path('themes/', StrategicThemePlanningListView.as_view(), name='theme_planning_list'),
    path('themes/<int:theme_id>/objectives/', StrategicObjectivePlanningListView.as_view(), name='objective_planning_list'),
    path('objectives/<int:strategic_objective_id>/kpis/', KPIPlanningListView.as_view(), name='kpi_planning_list'),
    path('reports/', ActivityReportView.as_view(), name='report_list'),
    path('reports/submit/<int:pk>/', SubmitReportView.as_view(), name='submit_report'),
]
