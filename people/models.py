# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, SlugField, ManyToManyField


@python_2_unicode_compatible
class User(AbstractUser):
    """User

    I don't know why I make it people.User though, but I do it anyway,
    easier access maybe?
    """
    def __str__(self):
        return self.username
