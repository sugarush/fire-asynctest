About
=====

Sugar Async Test provides an asynchronous test class for the python unittest
module.

Installation
============

Sugar Async Test can be installed with pip.

``pip install git+https://github.com/sugarush/sugar-asynctest@master``

Usage
=====

.. code-block:: python

  from sugar_asynctest import AsyncTestCase

  class TestSomethingAsync(AsyncTestCase):

    async test_something_async(self):
      ...
