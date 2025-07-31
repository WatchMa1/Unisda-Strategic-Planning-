from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404
from .deepseek import summarize_report
from strategic_planning.models import Report
import logging 

logger = logging.getLogger(__name__)

# Create your views here.

@csrf_exempt
@require_POST
def summarize_report_view(request, report_id):
    report = get_object_or_404(Report, id=report_id)

    try:
        summary = summarize_report(report.report_details)
        return JsonResponse({"summary": summary}, status=200)
    except Exception as e:
        logger.exception(f"Error summarizing report {report_id}: {e}")
        return JsonResponse({"error": "Failed to summarize report"}, status=500)