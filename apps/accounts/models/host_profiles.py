from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.base.models import CreatedTimeStampModel, HostType
from apps.accounts.models import AccountModel, LanguageModel


class HostProfileModel(CreatedTimeStampModel, models.Model):
    """ Профили зарегистрированных хозяев """
    host_name = models.CharField(unique=True, max_length=100, verbose_name=_('Имя хозяина'))
    account = models.OneToOneField(AccountModel,
                                   on_delete=models.PROTECT,
                                   related_name='host_profile')
    bio = models.TextField(blank=True, verbose_name=_('О себе'), )
    spoken_languages = models.ManyToManyField(LanguageModel,
                                              blank=True,
                                              related_name='hosts',
                                              verbose_name=_('Языки общения')
                                              )
    occupation = models.CharField(max_length=100, blank=True, verbose_name=_('Род занятий'), )
    host_type = models.CharField(max_length=20,
                                 choices=HostType,
                                 default=HostType.PRIVATE
                                 )

    class Meta:
        db_table = 'host_profiles'
        verbose_name = _('Профиль хозяина')
        verbose_name_plural = _('Профили хозяев')
        ordering = ['-created_at']

    def __str__(self):
        return self.host_name
