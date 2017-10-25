import sys
from threading import Thread

from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QPushButton
from multiprocessing import Process

try:
    import qdarkstyle
except ImportError:
    dark_style_available = False
else:
    dark_style_available = True

from PyQt5 import uic, QtWidgets

import player_api
from video import Video

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.dialog_load_new_video = LoadVideoDialog()
        self.setWindowTitle("Video Queuer")

        uic.loadUi('player.ui', self)

        self.setup_columns()

        self.threads = []
        self.videos = []

        self.button_load_new_video.clicked.connect(self.load_new_video_clicked)
        self.button_stop_all.clicked.connect(self.stop_all_clicked)
        self.button_override.clicked.connect(self.override_clicked)

    def setup_columns(self):
        self.table_videos.setColumnWidth(0, 500)
        self.table_videos.setColumnWidth(1, 130)
        self.table_videos.setColumnWidth(2, 130)

    def refresh_rows(self):
        print(self.videos)
        num_videos = len(self.videos)
        self.table_videos.setRowCount(num_videos)
        for i, video in zip(range(num_videos), self.videos):
            print(video.filename)
            self.table_videos.setItem(i, 0, QTableWidgetItem(video.filename))
            time = "%02d:%02d:%02d" % (video.hour, video.minute, video.second)
            self.table_videos.setItem(i, 2, QTableWidgetItem(time))
            button = QPushButton()
            button.setText("Delete")
            # self.table_videos.setCellWidget(i, 3, button)

    def load_new_video_clicked(self):
        name, time = self.dialog_load_new_video.get_video()
        time_split = time.split(":")
        time_split = [int(x) for x in time_split]
        print(time_split)
        # TODO - manual start, loop

        def wrapper():
            self.schedule_on_thread(time_split, name)

        thread = Process(name=name,target=wrapper)#Thread(name=name, target=wrapper)
        thread.start()
        self.threads.append(thread)
        # video = Video(time_split[0], time_split[1], time_split[2], name, ["--fullscreen"])
        # video.start_clock()

    def schedule_on_thread(self, time_split, name):
        video = Video(time_split[0], time_split[1], time_split[2], name, [])  # ["--fullscreen"]
        self.videos.append(video)
        self.videos.sort(key=lambda x: (x.hour, x.minute, x.second))
        self.refresh_rows()
        video.start_clock()

    @staticmethod
    def stop_all_clicked():
        player_api.stop()

    def override_clicked(self):
        """
        Run the first video in the queue. If this is set to play manually,
        it will just be played. If this is already scheduled for a time,
        the time will be removed and the video will be played now.
        """
        # note this is assuming that the videos are sorted - the
        # insert function does this already, but we need to look into
        # when we load video queue from a file
        # self.videos[0].hour = -1
        # self.videos[0].minute = -1
        # self.videos[0].second = -1
        # self.videos[0].play()


class LoadVideoDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi("load_video_dialog.ui", self)

        self.button_choose_video.clicked.connect(self.button_choose_video_clicked)
        self.buttonbox_load_new_video.accepted.connect(self.load_new_video_clicked)
        self.file_dialog = QtWidgets.QFileDialog

        self.isAccepted = False
        self.video_file_name = ""

    def button_choose_video_clicked(self):
        self.video_file_name = self.file_dialog.getOpenFileName(self, "Load Video File",
                                                                "", "MP4 Files (*.mp4);;")
        self.label_load_video_name.setText(self.video_file_name[0].split("/")[-1])

    def load_new_video_clicked(self):
        self.isAccepted = True

    def get_selected_video(self):
        return self.video_file_name[0]

    def get_play_time(self):
        return self.lineedit_start_time.text()

    # static method to create the dialog and return (video, time)
    @staticmethod
    def get_video():
        dialog = LoadVideoDialog()
        dialog.exec_()
        video = dialog.get_selected_video()
        time = dialog.get_play_time()
        return video, time


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    if dark_style_available:
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = Window()
    w.show()

    sys.exit(app.exec_())
