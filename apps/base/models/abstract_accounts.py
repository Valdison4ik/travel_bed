from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedAccountModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name="%(class)s_created",
        verbose_name=_('Кто создал')
    )

    class Meta:
        abstract = True


class UpdatedAccountModel(models.Model):
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
class DeletedAccountModel(models.Model):
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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