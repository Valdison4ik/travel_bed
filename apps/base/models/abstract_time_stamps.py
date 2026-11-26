from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Когда создано'))

    class Meta:
        abstract = True


class UpdatedTimeStampModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Когда изменено'))

    class Meta:
        abstract = True

"""

class DeletedTimeStampModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name=_('Когда удалено'))

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    class Meta:
        abstract = True
"""