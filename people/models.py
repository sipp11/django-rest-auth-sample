# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser


@python_2_unicode_compatible
class User(AbstractUser):
    """User

    Extending AbstractUser is the easiest way to have custom fields for
    user model.
    """
    def __str__(self):
        return self.username
