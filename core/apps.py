from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        def create_superuser(sender, **kwargs):
            USERNAME = "admin"  # change to your desired username
            EMAIL = "admin@example.com"  # change to your desired email
            PASSWORD = "password123"  # change to your desired password

            if not User.objects.filter(username=USERNAME).exists():
                User.objects.create_superuser(
                    username=USERNAME,
                    email=EMAIL,
                    password=PASSWORD
                )
                print("Superuser created successfully!")

        post_migrate.connect(create_superuser, sender=self)
