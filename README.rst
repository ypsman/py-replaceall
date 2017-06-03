replaceall
**********

replaceall is a Python 2.7/3 module to replace
or remove one or more Chars from a given string.


Installation
============

    $ pip install replaceall

or

    $ easy_install replaceall

Usage & Example
===============

remove single Char

.. code-block:: python

    from replaceall import replaceall
    name = replaceall("John Doe!", "!")
    print(name)
    "John Doe"

replace Chars

.. code-block:: python

    from replaceall import replaceall
    name = replaceall("John Doe#", "#", "!")
    print(name)
    "John Doe!"

also works with Lists

.. code-block:: python

    from replaceall import replaceall
    replaceCharlist = ["!","@", "#"]
    name = replaceall("John@Doe#.foo", replaceCharlist, ".")
    print(name)
    "John.Doe.foo"
