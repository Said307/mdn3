
import re
from django.core.exceptions import ValidationError

class UppercaseValidator:
    """ The password must contains at least 1 uppercase letter"""

    def validate(slef,password,user=None):
        if not re.findall('A-Z',password):
            raise ValidationError(
                "The password must contain at least 1 uppercase letter, A-Z."
                )
    def get_help_text(self):
        return("Your password must contain at least 1 uppercase letter, A-Z.")


class MinimumLengthValidator:
   
    def __init__(self,min_length=5):
        self.min_length = min_length

    def validate(self,password,user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                "This password must contain at least %(min_length)d characters.",params={'min_length': self.min_length}

            )


    def get_help_text(self):
        return (
            "Your password must contain at least %(min_length)d characters."
            % {'min_length': self.min_length}
        )