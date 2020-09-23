==========
zeitsprung
==========

.. image:: https://img.shields.io/pypi/v/zeitsprung.svg
        :target: https://pypi.python.org/pypi/zeitsprung

.. image:: https://img.shields.io/travis/munterfinger/zeitsprung.svg
        :target: https://travis-ci.com/munterfinger/zeitsprung

.. image:: https://readthedocs.org/projects/zeitsprung/badge/?version=latest
        :target: https://zeitsprung.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
.. image:: https://pyup.io/repos/github/munterfinger/zeitsprung/shield.svg
     :target: https://pyup.io/repos/github/munterfinger/zeitsprung/
     :alt: Updates

This package provides a scraper for www.zeitsprung.fm, a great history podcast.
To get all episodes from the website, simply start the scraper::

    from zeitsprung.scrape import Scraper
    s = Scraper('path/to/folder/for/database')
    s.run()

This should download the all episode metadata and save the audio files in
'.wav' format to the specified folder.

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

* https://www.zeitsprung.fm
* This package is licensed under MIT, see the LICENSE file for details.
