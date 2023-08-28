import os
from django.core.wsgi import get_wsgi_application

# Replace 'Django_project' with the name of your Django project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_project.settings')

application = get_wsgi_application()
