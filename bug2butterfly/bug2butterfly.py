#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This module does
    Date created: 4/20/2016
    Date last modified: 4/25/2016
    Python Version: 2.7.10
"""
from __future__ import print_function

__author__ = "pengwk"
__copyright__ = "Copyright 2016, pengwk"
__credits__ = [""]
__license__ = "Private"
__version__ = "0.1"
__maintainer__ = "pengwk"
__email__ = "pengwk2@gmail.com"
__status__ = "BraveHeart"

import sys

import logging
import traceback

logging.basicConfig(filename="bug2butterfly.txt", level=logging.DEBUG)


def butterfly(func):
    from functools import wraps

    @wraps(func)
    def wrapper(*arg, **kwargs):
        def bug(*arg, **kwargs):
            try:
                func(*arg, **kwargs)
            except:
                # 记录错误
                _type, _value, _traceback = sys.exc_info()
                logging.error(sys.exc_info())
                logging.error(traceback.extract_tb(_traceback))
                logging.error(traceback.format_exc())
                raise

        return bug(*arg, **kwargs)

    return wrapper


def test():
    @butterfly
    def my_fault(a, b):
        print(a / b)

    my_fault(2, 0)


def main():
    return None


if __name__ == "__main__":
    test()
