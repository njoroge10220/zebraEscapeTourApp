from django.apps import AppConfig


class TourConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tour'
    

class YourAppConfig(AppConfig):
    name = 'tourApp'

    def ready(self):
        import tourApp.signals
