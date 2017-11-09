"""
This script handles I/O of schedule database files(named ".db")
They use standard SQLite3 format
For each schedule file, one creates a new instance of the Schedule class
This class will keep track of its file name, and handle reading and writing of
that file.
"""

import sqlite3

from video import Video


class Schedule:
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, " \
                   "hour INTEGER, minute INTEGER, second INTEGER, flags TEXT)"
    RENAME_TABLE = "ALTER TABLE {} RENAME TO {}"
    INSERT_NEW = "INSERT INTO {} (hour,minute,second,flags) VALUES " \
                 "(?,?,?,?)"
    SELECT_ALL = "SELECT * FROM {}"
    SELECT_BY_ID = "SELECT * FROM {} WHERE id=?"

    def __init__(self, table_name: str = "default"):
        self.table_name = table_name

        cursor = connection.cursor()
        cursor.execute(self.CREATE_TABLE.format(self.table_name))
        connection.commit()     # NOTE: NOT "cursor.commit()"

    def rename(self, new_name: str = "default"):
        cursor = connection.cursor()
        cursor.execute(self.RENAME_TABLE.format(self.table_name, new_name))
        connection.commit()

        self.table_name = new_name

    def insert(self, video: Video):
        cursor = connection.cursor()
        cursor.execute(self.INSERT_NEW.format(self.table_name), (video.filename,
                                                                 video.hour, video.minute,
                                                                 video.second,
                                                                 ",".join(video.flags)))
        connection.commit()


connection = sqlite3.connect("schedules.vstx")
