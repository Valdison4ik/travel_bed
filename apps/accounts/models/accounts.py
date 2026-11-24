from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.db import models

from apps.base.models import CreatedTimeStampMixin, UpdatedTimeStampMixin


class AccountModel(AbstractBaseUser,
                   PermissionsMixin,
                   CreatedTimeStampMixin,
                   UpdatedTimeStampMixin
                   ):
    username = models.CharField(_('Имя пользователя'),
                                unique=True,
                                max_length=50,
                                error_messages={"unique": _("A user with that username already exists."),
                                                })
    first_name = models.CharField(_('Имя'), unique=True, max_length=80, validators=[MinLengthValidator(2)])
    last_name = models.CharField(_("Фамилия"), max_length=120, validators=[MinLengthValidator(2)])
    email = models.EmailField(_('Электронный адрес'),
                              unique=True,
                              error_messages={"unique": _("A user with that email already exists."),
                                              })
    avatar = models.FileField(blank=True, verbose_name=_('Фото профиля'))
    # phone = models.CharField(_('Номер телефона'), max_length=15, null=True, blank=True)
    is_staff = models.BooleanField(_('Является ли сотрудником'), default=False)
    is_active = models.BooleanField(_('Является ли активным'), default=True)
    last_login = models.DateTimeField(_('Последнее подключение'), null=True,
                                      blank=True)  # Поле даты и времени, заполняется при входе в систему

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['-last_login']
        # constraints = [models.UniqueConstraint(fields=['name', 'project'], name='unique_name_project')]

    def __str__(self):
        return f'{self.username}, {self.email}'

    # !!! через ExpressionWrapper в кастомном Manager или QuerySet
    @property
    def account_age(self):
        return timezone.now() - self.created_at

    USERNAME_FIELD = "email"
