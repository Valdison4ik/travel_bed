from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _


class LanguageModel(models.Model):
    code = models.CharField(unique=True,
                            max_length=3,
                            validators=[MinLengthValidator(2)
                                        # RegexValidator(regex=r'^[a-z]{2-3}$',)
                                        ],
                            )  # 'ru', 'en', 'de'
    title = models.CharField(max_length=50, verbose_name=_('Международное название языка'))

    class Meta:
        db_table = 'language'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['code']

    def __str__(self):
        return self.title
