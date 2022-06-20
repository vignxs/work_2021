from suit.apps import DjangoSuitConfig
from django.apps import AppConfig


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

