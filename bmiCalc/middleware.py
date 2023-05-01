from django.http import HttpResponse

class CSPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("CSPMiddleware is called")
        response = self.get_response(request)

        if getattr(request, "CSP_MIDDLEWARE_ENABLED", False):
            response['Content-Security-Policy'] = "default-src {}; style-src {};".format(
                ' '.join(request.CSP_DEFAULT_SRC),
                ' '.join(request.CSP_STYLE_SRC)
            )

        return response