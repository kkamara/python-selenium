import logging
import time

from django_ratelimit.decorators import ratelimit

request_logger = logging.getLogger("request")


# Propagate request logs to the root logger, which is configured to write to file.
class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        response = self.get_response(request)
        duration_ms = (time.perf_counter() - start_time) * 1000

        request_logger.info(
            "%s %s %s %.1fms",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
        )

        return response


class AdminRateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = ratelimit(key="ip", rate="50/h")

    def __call__(self, request):
        if request.path.startswith("/admin/"):
            return self.rate_limit(self.get_response)(request)  # Apply rate limit check
        return self.get_response(request)
