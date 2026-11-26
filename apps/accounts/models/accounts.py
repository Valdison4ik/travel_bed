from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.functions import Lower

from apps.base.models import CreatedTimeStampModel, UpdatedTimeStampModel


class AccountModel(AbstractBaseUser,
                   PermissionsMixin,
                   CreatedTimeStampModel,
                   UpdatedTimeStampModel
                   ):
    username = models.CharField(_('Имя пользователя'), max_length=50, )
    first_name = models.CharField(_('Имя'), max_length=80, validators=[MinLengthValidator(2)])
    last_name = models.CharField(_("Фамилия"), max_length=120, validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True,
                              error_messages={
                                  "unique": _('Пользователь с таким адресом электронной почты уже существует.'),
                                  },
                              verbose_name=_('Электронный адрес'), )
    avatar = models.ImageField(blank=True, verbose_name=_('Фото профиля'), )
    is_staff = models.BooleanField(_('Является ли сотрудником'), default=False)
    is_active = models.BooleanField(_('Является ли активным'), default=True)

    # Поле даты и времени, заполняется при входе в систему
    # не переопределяем: уже существует в AbstractBaseUser
    # last_login = models.DateTimeField(_('Последнее подключение'), null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'accounts'
        verbose_name = _('Учетная запись пользователя')
        verbose_name_plural = _('Учетные записи пользователей')
        ordering = ['-last_login']
        constraints = [models.UniqueConstraint(Lower('email'), name='unique_lower_email'),
                       ]

    def __str__(self):
        return f'{self.username}, {self.email}'

    # !!! через ExpressionWrapper в кастомном Manager или QuerySet
    # @property
    # def account_age(self):
    #     return timezone.now() - self.created_at

    USERNAME_FIELD = "email"
