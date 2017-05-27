#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import logging
import traceback

_format = """
## `%(exc_type)s`

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
    d = {'exc_type': exc_type,
         'traceback': "".join(traceback.format_exception(*exc_info))
         }
    logging.error("",
                  extra=d,
                  )
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


sys.excepthook = butterfly_hook


def test_butterfly():
    assert print(1 / 0)


def main():
    return None


