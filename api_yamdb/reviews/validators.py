import datetime

from django.core.exceptions import ValidationError


def validate_custom_year(value):
    if value > datetime.datetime.now().year:
        raise ValidationError('Дата выхода произведения',
                              'не может быть больше текущего года')
