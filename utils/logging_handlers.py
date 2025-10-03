import logging
import traceback
import requests

from django.conf import settings
from django.utils.log import AdminEmailHandler
from django.views.debug import get_exception_reporter_class


class ApiEndpointErrorHandler(logging.Handler):
    """
    A custom logging handler that sends a detailed error report to a
    specified API endpoint via a POST request.

    Reads the endpoint URL and an optional auth token from Django settings.
    """
    def __init__(self):
        super().__init__()
        # We can also add filters here if needed, e.g., self.addFilter(...)

    def emit(self, record):
        """
        This method is called for each log record.
        """
        # Get API configuration from settings
        api_endpoint = getattr(settings, 'ERROR_REPORTING_ENDPOINT', None)
        api_token = getattr(settings, 'ERROR_REPORTING_TOKEN', None)

        if not api_endpoint:
            # If no endpoint is configured, do nothing.
            return

        try:
            request = record.request
            # Use Django's built-in reporter to get rich exception details
            reporter = get_exception_reporter_class(request)(request, *record.exc_info)
            html_report = reporter.get_traceback_html()

            payload = {
                "phone": getattr(settings, 'ADMIN_PHONE', None),
                "message": f'''
level: {record.levelname},
message :{self.format(record)},
html_report: {html_report},
                '''
            }
            headers = {}
            if api_token:
                headers["Authorization"] = f"Bearer {api_token}"

            requests.post(api_endpoint, data=payload, headers=headers)

        except Exception:
            # If the handler itself fails, write to stderr.
            self.handleError(record)