import sys
import qdarkstyle

from PyQt5 import uic, QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.dialog_load_new_video = LoadVideoDialog()
        self.setWindowTitle("Video Queuer")

        uic.loadUi('player.ui', self)

        self.setup_columns()

        self.button_load_new_video.clicked.connect(self.load_new_video_clicked)

    def setup_columns(self):
        self.table_videos.setColumnWidth(0, 500)
        self.table_videos.setColumnWidth(1, 130)
        self.table_videos.setColumnWidth(2, 130)

    def load_new_video_clicked(self):
        print(self.dialog_load_new_video.get_video())


class LoadVideoDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi("load_video_dialog.ui", self)

        self.button_choose_video.clicked.connect(self.button_choose_video_clicked)
        self.buttonbox_load_new_video.accepted.connect(self.load_new_video_clicked)
        self.file_dialog = QtWidgets.QFileDialog

        self.isAccepted = False

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
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = Window()
    w.show()

    sys.exit(app.exec_())
