成蝶 bug2butterfly
---------------------

.. image:: https://img.shields.io/pypi/v/bug2butterfly.svg
    :target: https://pypi.python.org/pypi/bug2butterfly

.. image:: https://img.shields.io/pypi/l/bug2butterfly.svg
    :target: https://pypi.python.org/pypi/bug2butterfly

.. image:: https://img.shields.io/pypi/pyversions/bug2butterfly.svg
    :target: https://pypi.python.org/pypi/bug2butterfly

.. image:: https://travis-ci.org/pengwk/bug2butterfly.svg?branch=master
    :target: https://travis-ci.org/pengwk/bug2butterfly

.. image:: https://travis-ci.org/pengwk/bug2butterfly.svg?branch=master
    :target: https://travis-ci.org/pengwk/bug2butterfly

为新手准备，记录出现的每一个异常！



安装 Installation
----------------

To install bug2butterfly, simply:

.. code-block:: bash

    $ pip install bug2butterfly

如何使用 Usage
-------------

在需要的程序中导入即可

.. code-block:: python

    import bug2butterfly

项目目录下会生成一个`butterflies.md`文件，内容像下面这样：

`<type 'exceptions.ZeroDivisionError'>`
=======================================

2017/05/24 08:07:56 PM - root - ERROR



.. code-block:: python

    Traceback (most recent call last):
        File "E:/pengwk_project/bug2butterfly/bug2butterfly/bug2butterfly.py", line 84, in <module>
            hook_test()
        File "E:/pengwk_project/bug2butterfly/bug2butterfly/bug2butterfly.py", line 76, in hook_test
            print(1 / 0)
    ZeroDivisionError: integer division or modulo by zero


Contributing
------------

We welcome contributions! If you would like to hack on Flask-Login, please
follow these steps:

1. Fork this repository
2. Make your changes
3. Submit a pull request (ensure it does not error!)

Please give me adequate time to review your submission. Thanks!
