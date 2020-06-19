from django.apps import AppConfig


class UseraccountsConfig(AppConfig):
    name = 'useraccounts'

    def ready(self):
        import useraccounts.signals
