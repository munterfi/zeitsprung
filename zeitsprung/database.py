from pandas import DataFrame, to_datetime
from sqlite3 import connect
from unicodedata import normalize
from zeitsprung.base import Base


class SQLiteEngine(Base):
    """ Class to set up and access a SQLite database to store the data from zeitsprung.fm """
    def __init__(self, db_file: str, verbose: bool = True) -> None:
        super().__init__(verbose)
        self.db_file = db_file
        self.verbose = verbose

    def create_connection(self):
        conn = None
        try:
            conn = connect(self.db_file)
        except BaseException as e:
            print(e)
        return conn

    def setup_schema(self):
        self._print(f"Setting up SQLite database at '{self.db_file}'.")
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS meta;')
        cur.execute('''
        CREATE TABLE meta (
            uid INTEGER PRIMARY KEY,
            published_at DATETIME NOT NULL,
            modified_at DATETIME NOT NULL,
            abbreviation TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            url_episode TEXT NOT NULL,
            url_audio TEXT NOT NULL
        );
        ''')
        cur.execute('DROP TABLE IF EXISTS audio;')
        cur.execute('''
        CREATE TABLE audio (
            uid INTEGER PRIMARY KEY,
            file_path TEXT NOT NULL,
            duration INTEGER NOT NULL,
            frame_rate INTEGER NOT NULL,
            frame_width INTEGER NOT NULL
        );
        ''')
        conn.commit()
        conn.close()

    def insert_meta_row(self, row: list):
        self._print(f"Writing row for '{row[0]}' to table 'meta'.")
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
        INSERT INTO meta (uid, published_at, modified_at, abbreviation, title, description, url_episode, url_audio)
        VALUES('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{normalize("NFKD", row[4]).replace("'", '')}',
            '{normalize("NFKD", row[5]).replace("'", '')}', '{row[6]}', '{row[7]}');
        """)
        conn.commit()
        conn.close()

    def insert_audio_row(self, row: list):
        self._print(f"Writing row for '{row[0]}' to table 'audio'.")
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(f"""
        INSERT INTO audio (uid, file_path, duration, frame_rate, frame_width)
        VALUES('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}');
        """)
        conn.commit()
        conn.close()

    def query_last_episode_id(self):
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute('SELECT max(uid) FROM meta')
        uid = cur.fetchall()[0][0]
        return 0 if uid is None else uid

    def query_all_meta(self):
        self._print("Querying all rows from table 'meta'.")
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM meta')
        rows = cur.fetchall()
        conn.close()
        df = DataFrame([list(row) for row in rows],
                       columns=['uid', 'published_at', 'modified_at', 'abbreviation',
                                'title', 'description', 'url_episode', 'url_audio'])
        df['published_at'] = to_datetime(df['published_at'])
        df['modified_at'] = to_datetime(df['modified_at'])
        return df

    def query_all_audio(self):
        self._print("Querying all rows from table 'audio'.")
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM audio')
        rows = cur.fetchall()
        conn.close()
        df = DataFrame([list(row) for row in rows],
                       columns=['uid', 'file_path', 'duration', 'frame_rate', 'frame_width'])
        return df
