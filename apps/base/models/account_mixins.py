import os
# import django
from django.db import models
from django.utils.translation import gettext_lazy as _

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()

class CreatedAccountMixin(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name="%(class)s_created",
        verbose_name=_('Кто создал')
    )

    class Meta:
        abstract = True


class UpdatedAccountMixin(models.Model):
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name="%(class)s_updated",
        verbose_name=_('Кто изменил')
    )

    class Meta:
        abstract = True

"""
class DeletedAccountMixin(models.Model):
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name="%(class)s_deleted",
        verbose_name=_('Кто удалил')
    )

    class Meta:
        abstract = True

"""