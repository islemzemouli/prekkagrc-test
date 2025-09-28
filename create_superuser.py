import os
import django

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from django.contrib.auth.models import User

# Change these to your test credentials
USERNAME = "admin"
EMAIL = "admin@example.com"
PASSWORD = "admin123"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")
