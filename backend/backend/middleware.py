import logging
from django.utils.deprecation import MiddlewareMixin

logging.basicConfig(level=logging.INFO, filename="logs.log",
                    format="%(asctime)s - %(message)s")


class LoggingNameofMethods(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/api/'):
            logging.info(f"Название метода: {view_func.__name__}")
        return None
