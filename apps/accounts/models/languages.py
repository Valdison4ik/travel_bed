from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _


class LanguageModel(models.Model):
    code = models.CharField(unique=True,
                            max_length=3,
                            validators=[MinLengthValidator(2)],
                            )  # 'ru', 'en', 'de'
    title = models.CharField(max_length=50, verbose_name=_('Международное название языка'))

    class Meta:
        db_table = 'languages'
        verbose_name = _('Язык')
        verbose_name_plural = _('Языки')
        ordering = ['code']

    def __str__(self):
        return self.title
