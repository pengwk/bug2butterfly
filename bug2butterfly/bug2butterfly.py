#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import traceback

# issue _my_fault is connected with record
_format = """
## `{exc_type}`

%(asctime)s - %(name)s - %(levelname)s - %(message)s

```
{traceback}
```
"""


def butterfly_hook(exc_type, exc_value, exc_traceback):

    # exc_info = (_test, exc_value, exc_traceback)

    traceback_content = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    except_item = _format.format(exc_type=exc_type, traceback=traceback_content)
    with open('butterfly.md', 'a') as f:
        f.write(except_item)

    sys.__excepthook__(exc_type, exc_value, exc_traceback)


sys.excepthook = butterfly_hook
