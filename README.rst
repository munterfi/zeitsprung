.. image:: https://raw.githubusercontent.com/munterfi/zeitsprung/master/docs/_static/logo.svg
   :width: 120 px
   :alt: zeitsprung.fm
   :align: right

==========
zeitsprung
==========

.. image:: https://img.shields.io/pypi/v/zeitsprung.svg
        :target: https://pypi.python.org/pypi/zeitsprung

.. image:: https://github.com/munterfi/zeitsprung/workflows/build/badge.svg
        :target: https://github.com/munterfi/zeitsprung/actions?query=workflow%3Abuild

.. image:: https://readthedocs.org/projects/zeitsprung/badge/?version=latest
        :target: https://zeitsprung.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/munterfi/zeitsprung/shield.svg
        :target: https://pyup.io/repos/github/munterfi/zeitsprung/
        :alt: Updates

.. image:: https://codecov.io/gh/munterfi/zeitsprung/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/munterfi/zeitsprung

Note: zeitsprung.fm has moved to geschichte.fm, therefore this project is no longer maintained.

This package provides a scraper for www.zeitsprung.fm, a great history podcast.
To get the metadata of all episodes from the website, simply start the scraper::

    from zeitsprung.scraping import Scraper
    s = Scraper('path/to/folder/for/database')
    s.run()

The scraper then downloads the all episode metadata and audio files. The metadata is written to the 'meta' table in the
database. The audio files are converted to '.wav' files and saved separately to a folder, while a link to the file is
stored in the 'audio' table in the database.

To access the data, create a SQLiteEngine::

    from zeitsprung.database import SQLiteEngine
    db = SQLiteEngine('path/to/folder/for/database/zeitsprung.db')

Query the meta data from the database::

    db.query_all_meta()

And the audio file paths and meta data::

    db.query_all_audio()

Now have fun with analysing the episodes of zeitsprung!

Features
--------

* Scraper class to download the meta data and audio files of all episodes.
* Database class to setup and access the SQLite database containing the meta data of the episodes.

To Do
-----

* Processing class to conduct speech recognition on the audio files and build an index for clustering the topics.
* Visualize up to date statistics.

References
----------

* https://www.zeitsprung.fm, check it out!
* This package is licensed under MIT, see the LICENSE file for details.
