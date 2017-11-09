"""
This script handles I/O of schedule files(.vstx)
For each schedule file, one creates a new instance of the Schedule class
This class will keep track of its file name, and handle reading and writing of
that file.
"""

import sqlite3


class Schedule:
    CREATE_TABLE_VIDEOS = "CREATE TABLE IF NOT EXISTS videos"
    INSERT_NEW = "INSERT INTO "
    def __init__(self, filename: str = "default.vstx"):
        self.filename = filename

    def insert(self):
        conn = sqlite3.connect(database=self.filename)
        c = conn.cursor()
        cursor.ins
        f.write()