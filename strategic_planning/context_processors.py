

from .models import StrategicTheme

def strategic_themes(request):
    return {
        'strategic_themes': StrategicTheme.objects.all(),
    }