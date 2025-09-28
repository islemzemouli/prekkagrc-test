from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        def create_superuser(sender, **kwargs):
            from django.contrib.auth.models import User  # <-- import inside
            USERNAME = "admin"
            EMAIL = "admin@example.com"
            PASSWORD = "Password123"

            if not User.objects.filter(username=USERNAME).exists():
                User.objects.create_superuser(
                    username=USERNAME,
                    email=EMAIL,
                    password=PASSWORD
                )
                print("Superuser created successfully!")

        post_migrate.connect(create_superuser, sender=self)
