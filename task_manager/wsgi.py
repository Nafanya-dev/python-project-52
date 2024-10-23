import os

from django.core.wsgi import get_wsgi_application
import rollbar
from django.conf import settings


rollbar.init(**settings.ROLLBAR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

application = get_wsgi_application()
