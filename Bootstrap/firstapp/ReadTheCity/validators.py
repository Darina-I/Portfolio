import re
import datetime

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

#проверка на буквы верхнего регистра
def clean_password(value):
    if len(value) < 8:
        raise ValidationError("Пароль должен состоять минимум из 8 символов")
    if not re.findall('[A-ZА-Я]', value):
        raise ValidationError("Пароль должен содержать как минимум одну заглавную букву")
    elif not re.findall('[@#$%!^&*]', value):
        raise ValidationError("Пароль должен содержать как минимум один спец символ: " +
                              "@#$%!^&*")
    else:
        return value

def clean_email(value):
    #если в текущей модели User существует записи с указанным email, то условие сработает
    if get_user_model().objects.filter(email=value).exists():
        raise ValidationError("Такой E-mail уже существует")
    else:
        return value

def clean_year(value):
    if not value.isdigit():
        raise ValidationError("Введен некорректный год")
    else:
        year = int(value)
        now_year = datetime.date.today().year
        if not re.match(r"^\d{4}$", value):
            raise ValidationError("Введен некорректный год")
        elif year > now_year:
            raise ValidationError("Введен некорректный год")
        else:
            return value
def clean_isbn(value):
    if len(value) == 13:
        return value
    else:
        raise ValidationError("ISBN введен некорректно")

def clean_date(value):
    now = datetime.date.today ()
    if value > now:
        raise ValidationError("Дата введена некорректно")
    else:
        return value
