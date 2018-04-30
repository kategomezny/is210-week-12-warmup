#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """InvalidAgeError class"""
    pass

def get_age(birthyear):
    """converting birth year to age."""
    if birthyear >= datetime.datetime.now().year:
        raise InvalidAgeError
    else:
        age = datetime.datetime.now().year - birthyear
        return age
