from django.urls import path
from . import views
from .views import (
    AchievementCreateView, AchievementDeleteView, AchievementDetailView, AchievementListView, AchievementUpdateView, HomeView, LoginView, MainActivityCreateView, MainActivityUpdateView, ReportCreateView, ReportDetailView, ReportListView, ReportUpdateView, RoleCreateView, RoleDetailView, RoleListView, RoleUpdateView,StrategicThemeListView, StrategicThemeDetailView, StrategicThemeCreateView, StrategicThemeUpdateView, StrategicThemeDeleteView,
    StrategicObjectiveListView, StrategicObjectiveDetailView, StrategicObjectiveCreateView, StrategicObjectiveUpdateView, StrategicObjectiveDeleteView,
    DesignationListView, DesignationDetailView, DesignationCreateView, DesignationUpdateView, DesignationDeleteView,
    KPIListView, KPIDetailView, KPICreateView, KPIUpdateView, KPIDeleteView,
    ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView, UserCreateView, UserListView, UserUpdateView
)

urlpatterns = [
    path('main-activity/create/', MainActivityCreateView.as_view(), name='main_activity_create'),
    path('main-activity/update/', MainActivityUpdateView.as_view(), name='main_activity_update'),
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
    
    path('achievements/', AchievementListView.as_view(), name='achievement_list'),
    path('achievements/<int:pk>/', AchievementDetailView.as_view(), name='achievement_detail'),
    path('achievements/create/', AchievementCreateView.as_view(), name='achievement_create'),
    path('achievements/<int:pk>/update/', AchievementUpdateView.as_view(), name='achievement_update'),
    path('achievements/<int:pk>/delete/', AchievementDeleteView.as_view(), name='achievement_delete'),
    
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
]
