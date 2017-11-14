"""
This script handles I/O of schedule database files(named ".db")
They use standard SQLite3 format
For each schedule file, one creates a new instance of the Schedule class
This class will keep track of its file name, and handle reading and writing of
that file.
"""

import sqlite3

from video import Video


class DBManager:
    """
    This class does not create any tables. Its sole purpose is to manage the
    SQLite database that we are saving everything inside.
    """

    def __init__(self, db_name: str = "schedules.vstx"):
        self.connection = sqlite3.connect(db_name)

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


class Schedule:
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, " \
                   "hour INTEGER, minute INTEGER, second INTEGER, filename TEXT ," \
                   "flags TEXT)"
    RENAME_TABLE = "ALTER TABLE {} RENAME TO {}"
    INSERT_NEW_VIDEO = "INSERT INTO {} (hour,minute,second,filename,flags) VALUES " \
                       "(?,?,?,?,?)"
    SELECT_ALL_VIDEOS = "SELECT * FROM {}"
    SELECT_TABLE_NAMES = "SELECT name FROM sqlite_master WHERE type='table' " \
                         "ORDER BY name"
    SELECT_BY_ID = "SELECT * FROM {} WHERE id=?"
    UPDATE_VIDEO = "UPDATE {} SET hour=?, minute=?, second=?, filename=? WHERE id=?"
    DELETE_VIDEO = "DELETE FROM {} WHERE id=?"
    CLEAR_VIDEOS = "DELETE FROM {}"

    def __init__(self, connection, table_name: str = "schedule_1"):
        self.table_name = table_name

        self.connection = connection

        if not self.is_open():
            return

        self.connection = connection

        cursor = self.connection.cursor()
        cursor.execute(self.CREATE_TABLE.format(self.table_name))
        self.connection.commit()  # NOTE: NOT "cursor.commit()"

        res = self.connection.execute(self.SELECT_TABLE_NAMES)
        for name in res:
            print(name[0])

    def is_open(self):
        try:
            self.connection.execute(self.SELECT_TABLE_NAMES)
        except sqlite3.ProgrammingError:
            return False
        else:
            return True

    def rename(self, new_name: str = "default"):
        if not self.is_open():
            return False

        cursor = self.connection.cursor()
        cursor.execute(self.RENAME_TABLE.format(self.table_name, new_name))
        self.connection.commit()

        self.table_name = new_name

        return True

    def insert(self, video: Video):
        if not self.is_open():
            return
        print("AUGH")

        cursor = self.connection.cursor()
        cursor.execute(self.INSERT_NEW_VIDEO
                       .format(self.table_name), (str(video.hour), str(video.minute), str(video.second),
                                                  video.filename,
                                                  ",".join(video.flags)))
        print(str(video.hour), str(video.minute), str(video.second), video.filename, "help")
        self.connection.commit()
        rowid = cursor.lastrowid
        print("Rowid", rowid)
        return rowid

    def list_all(self):
        if not self.is_open():
            return

        cursor = self.connection.cursor()
        cursor.execute(self.SELECT_ALL_VIDEOS.format(self.table_name))
        result = cursor.fetchall()
        videos = []
        for row in result:
            # TODO: figure out length
            print(row[1], "1st of row")
            videos.append(Video(row[1], row[2], row[3], row[4], row[5].split(","), "", True))
        return videos

    def update(self, video: Video):
        if not self.is_open():
            return

        cursor = self.connection.cursor()
        cursor.execute(self.UPDATE_VIDEO.format(self.table_name),
                       (video.hour, video.minute, video.second, video.filename, video.id))
        self.connection.commit()

    def delete(self, video: Video):
        if not self.is_open():
            return

        cursor = self.connection.cursor()
        cursor.execute(self.DELETE_VIDEO.format(self.table_name), (video.id,))
        self.connection.commit()

    def clear(self):
        if not self.is_open():
            return

        cursor = self.connection.cursor()
        cursor.execute(self.CLEAR_VIDEOS.format(self.table_name))
        self.connection.commit()


if __name__ == '__main__':
    with DBManager("schedules.vstx") as conn:
        schedule1 = Schedule(conn, "schedule_1")
        schedule1.clear()
        schedule1.insert(Video(5, 5, 5, "video_1", [], "1", True))
        schedule1.insert(Video(5, 5, 5, "video_2", [], "1", True))
        schedule1.insert(Video(5, 5, 5, "video_3", [], "1", True))
        print(schedule1.list_all())
