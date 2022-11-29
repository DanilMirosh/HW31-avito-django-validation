from datetime import date

from django.core.exceptions import ValidationError


def check_age(date_of_birth: date):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    if age < 9:
        raise ValidationError(f"Age is {age}, it may not be less than 9")


