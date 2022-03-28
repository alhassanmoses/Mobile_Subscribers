from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from user_account.models.User import User
from django.utils.translation import gettext_lazy as _
from subscriber.models.services import services


class MobileSubscriberModel(models.Model):

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    msisdn = models.CharField(
        validators=[phoneNumberRegex],
        max_length=16,
        unique=True
    )

    customer_id_owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='Customer_id_owner'
    )

    customer_id_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='Customer_id_user'
    )

    service_type = models.CharField(
        max_length=50,
        choices=services,
        default=0,
    )

    service_start_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.msisdn
