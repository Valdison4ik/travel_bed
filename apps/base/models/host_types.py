from django.db import models
from django.utils.translation import gettext_lazy as _


class HostType(models.TextChoices):
    PRIVATE = 'private', _('Частное лицо')
    AGENT = 'agent', _('Агент / Риелтор')
    COMPANY = 'company', _('Управляющая компания')
