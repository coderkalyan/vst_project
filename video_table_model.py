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
                value = ":".join([str(r.hour), str(r.minute), str(r.second)])
            else:
                value = "Manual Play"
        elif index.column() == 2:
            # TODO - duration
            value = "1:00"
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
        return 0

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
                ok = pattern1.match(value) or value == "-1" or value == "-1:-1:-1"
                if not ok:
                    return False

                h, m, s = value.split(":")
                if not h.isdigit() or not m.isdigit() or not s.isdigit():
                    return False
                self.data[index.row()].hour = h
                self.data[index.row()].minute = m
                self.data[index.row()].second = s
                print(self.data[index.row()])

        self.dataChanged.emit(index, index)
        return True

    """def contextMenuEvent(self, event):
        self.menu = QtGui.QMenu(self)
        renameAction = QtGui.QAction('Rename', self)
        renameAction.triggered.connect(lambda: self.renameSlot(event))
        self.menu.addAction(renameAction)
        # add other required actions
        self.menu.popup(QtGui.QCursor.pos())"""
