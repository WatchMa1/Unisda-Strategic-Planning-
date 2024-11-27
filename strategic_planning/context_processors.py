

from .models import StrategicTheme, StrategicObjective

def strategic_themes(request):
    return {
        'strategic_themes': StrategicTheme.objects.all(),
    }
    
def strategic_objectives_context(request):
    """
    Context processor to add strategic objectives to the global context.
    """
    if request.user.is_authenticated:
        # Filter objectives based on user designation
        user_designation = request.user.designation
        objectives = StrategicObjective.objects.filter(designation=user_designation)
    else:
        objectives = StrategicObjective.objects.none()  # Empty queryset for unauthenticated users

    return {
        'strategic_objectives': objectives,
    }
    
