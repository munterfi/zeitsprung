=====
Usage
=====

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
