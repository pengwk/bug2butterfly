#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This module does
    Date created: 4/20/2016
    Date last modified: 4/25/2016
    Python Version: 2.7.10
"""
from __future__ import print_function
import sys
import logging
import traceback

_format = """
## %(exc_type)s

%(asctime)s - %(name)s - %(levelname)s - %(message)s

```
%(traceback)s
```
"""

logging.basicConfig(filename="butterflies.md",
                    format=_format,
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.WARNING)


def butterfly_hook(exc_type, exc_value, exc_traceback):
    exc_info = (exc_type, exc_value, exc_traceback)
    d = {}
    d['exc_type'] = exc_type
    d['traceback'] = "".join(traceback.format_exception(*exc_info))
    logging.error("",
                  extra=d,
                  )
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


sys.excepthook = butterfly_hook


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


def decorator_test():
    @butterfly
    def my_fault(a, b):
        print(a / b)

    my_fault(2, 0)


def hook_test():
    print(1 / 0)


def main():
    return None


if __name__ == "__main__":
    hook_test()
