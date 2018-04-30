#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Attempts to access any index or key of var1."""
    try:
        return var1[var2]
    except IndexError:
        print 'Warning: Your index/key doesn\'t exist'
    except KeyError:
        print 'Warning: Your index/key doesn\'t exist'
    return var1

