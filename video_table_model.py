import warnings

import re
from PyQt5.QtCore import QAbstractTableModel, Qt

from video import Video


class VideoTableModel(QAbstractTableModel):
    """
    This is a table model for our videos QTableView
    It stores the data and manages the table
    """
    def __init__(self, parent, data, header):
        """
        :param parent: parent
        :param data: list of videos
        :param header: list of strings representing column header names
        """
        QAbstractTableModel.__init__(self, parent)
        self.data = data
        self.header = header
        print(data,header)

    def set_data(self, data):
        """
        Updates the data
        :param data: data to update
        """
        self.data = data

        # get the table to re-render
        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0),
                              self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()

    def rowCount(self, parent=None, *args, **kwargs):
        """
        :return: number of videos
        """
        return len(self.data)

    def columnCount(self, parent=None, *args, **kwargs):
        """
        :return: number of columns in table
        """
        return Video.num_columns()

    def data(self, index, role=None):
        """
        :param index: contains info about the location of the cell being retrieved:
        use index.row() and index.column()
        :param role:
        :return:
        """
        value = 0
        if not index.isValid():
            return 0
        if index.column() == 0:
            value = self.data[index.row()].filename
        elif index.column() == 1:
            r = self.data[index.row()]
            if r.hour != -1:
                # value = ":".join([str(r.hour), str(r.minute), str(r.second)])
                value = "{:02d}:{:02d}:{:02d}".format(r.hour, r.minute, r.second)
                # value = value.format()
            else:
                value = "Manual Play"
        elif index.column() == 2:
            value = self.data[index.row()].length
        if role == Qt.EditRole:
            return value
        elif role == Qt.DisplayRole:
            return value
        """elif role == Qt.CheckStateRole:
            if index.column() == 0:
                if self.data[index.row()][index.column()].isChecked():
                    return Qt.Checked
                else:
                    return Qt.Unchecked"""

    def headerData(self, col, orientation, role=None):
        """
        :param col: the column being asked about
        :param orientation:
        :param role:
        :return: the name of the specified column header
        """
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        """
        Specify different flags for cells, like editable, selectable, enabled, etc.
        :param index: cell that is being asked for
        :return: the flags for the requested cell
        """
        if not index.isValid():
            return 0
        if index.column() == 0 or index.column() == 2:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role=None):
        """
        Sets the data of a specified cell
        :param index: location of the specified cell
        :param value: value to set the cell to
        :param role:
        :return: if the data was set or not
        """
        print(role)
        if not index.isValid():
            return False
        if role == Qt.EditRole:
            if index.column() == 1:
                # change the time
                pattern1 = re.compile(".*:.*:.*")
                ok = (pattern1.match(value) or value == "-1" or value == "-1:-1:-1")
                if not ok:
                    return False

                if value == "-1":
                    self.data[index.row()].hour = -1
                    self.data[index.row()].minute = -1
                    self.data[index.row()].second = -1
                    return True

                h, m, s = value.split(":")
                if not h.lstrip('-').isdigit() or not m.lstrip('-').isdigit() or not s.lstrip('-').isdigit():
                    return False
                h, m, s = map(int, (h, m, s))
                self.data[index.row()].hour = h
                self.data[index.row()].minute = m
                self.data[index.row()].second = s
                print(self.data[index.row()])

        self.dataChanged.emit(index, index)
        return True


import platform, os

class tableManipulator():
    def table_dump(self):
        try:
            with open(self.location) as f:
                table = f.read().splitlines()
        except FileNotFoundError:
            f2 = open(self.location, "w+")
            f2.close()
            self.table_dump()
        # Change rows to amount of "queued" videos
        video_list = []
        times = []
        videos = []
        flags = []

        for row in table:
            print(row, "row")
            try:
                h, m, s, name, args = row.split(',')  # to be safe(and readable), always put the ' '
                print("Phase 1")
                h, m, s = map(int, (h, m, s))  # convert these to int
                print(name, "name")
                length = self.get_length(name)
                print(length, "length")
                times.append(":".join([str(h), str(m), str(s)]))
                videos.append(name)
                flags.append(args)
                print("Phase 2")
                # make sure video uses os-specific directory separator
                print("Not removed", name)
                name = name.replace("C:/", "")
                print("Removed", name)
                name_split = name.split("/")
                print("System: ", platform.system())
                if platform.system() == "Windows":
                    print("Windows!")
                    name_split.insert(0, "C:\\")
                    print(name_split, "splitname")
                    name = os.path.join(*name_split)
                else:
                    print(name_split, "splitname")
                    name = "/" + os.path.join(*name_split)

                print("Name:", name)
                if h != -1:
                    video_list.append(Video(h, m, s, name, ["--fullscreen"], length, True))
                else:
                    video_list.append(Video(h, m, s, name, ["--fullscreen"], length, False))
                    # print("Video list:", video_list)

                    # Enqueue videos for playing. If the video is set to play manually, do not enqueue.
                    # we need a list to keep track of these threads, so they can be stopped later
                    # if the video is deleted
                print(times, videos, flags, "total")
            except (IndexError, ValueError):
                print(row, "row-except")
                print("excepted")
                continue

        print("Video list:", video_list)
        model = VideoTableModel(None, video_list, ["Video File Name", "Play Time", "Duration"])
        self.ui.table_videos.setModel(model)

