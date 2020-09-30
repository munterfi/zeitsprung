#!/usr/bin/env python

"""Tests for `zeitsprung` package."""

from zeitsprung.database import SQLiteEngine
from zeitsprung.scraping import Scraper


def test_database(tmp_path):
    d = tmp_path / 'data'
    d.mkdir()
    db_file = d / 'zeitsprung.db'
    print(db_file)
    db = SQLiteEngine(db_file)
    assert type(db) is SQLiteEngine


def test_scraper(tmp_path):
    d = tmp_path / 'data'
    d.mkdir()
    db_file = d / 'zeitsprung.db'
    print(db_file)
    s = Scraper(db_file)
    assert type(s) is Scraper
