.. highlight:: shell

============
Installation
============

System dependencies
-------------------
The zeitsprung package depends on the pydub package, which needs ffmpeg to be installed on the system.

macOS (using homebrew):

.. code-block:: console

    $ brew install ffmpeg

Linux (using aptitude):

.. code-block:: console

    $ apt-get install ffmpeg libavcodec-extra

Stable release
--------------

To install zeitsprung, run this command in your terminal:

.. code-block:: console

    $ pip install zeitsprung

This is the preferred method to install zeitsprung, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for zeitsprung can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/munterfi/zeitsprung

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/munterfi/zeitsprung/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/munterfi/zeitsprung
.. _tarball: https://github.com/munterfi/zeitsprung/tarball/master
