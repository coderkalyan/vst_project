#!/usr/bin/python3
import sys
import threading

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QAbstractItemView, QHeaderView, QMenu
from ui.video1 import Ui_MainWindow as MainUI
import scheduler
from load_video_dialog import Ui_Dialog as LoadVideoDialog
from nothing_to_inspect import Ui_Dialog as NothingToInspectDialog
from video import Video
# binds all buttons to functions
from video_table_model import VideoTableModel


def bind():
    # Connect Main UI Load New button to Load New function
    # Inspector OK button bindings moved to inspector due to design limitations and human idiocy
    ui.inspector.clicked.connect(lambda: inspect(False))
    ui.loadnew.clicked.connect(lambda: inspect(True))
    ui2.button_choose_video.clicked.connect(select_video)
    ui.actionQuit.triggered.connect(app.quit)
    # ui.actionAbout.triggered.connect(credits_window.exec_)
    # TODO - help action


def open_vst():
    # opens a text file for reading and writing video entries
    global location

    with open("pointer.txt", "w+") as pointer:
        location = pointer.read()
        # if we read from empty file(just created), fill it with path to default table
        if location == "":
            location = "vstdefault.txt"
            pointer.write(location)
    table_dump()


# Dump all entries into a QTable for editing in the GUI
def table_dump():
    with open(location) as f:
        table = f.read().splitlines()
    # Change rows to amount of "queued" videos
    video_list = []
    times = []
    videos = []
    flags = []

    for row in table:
        try:
            h, m, s, name, args = row.split(' ')  # to be safe(and readable), always put the ' '
            h, m, s = map(int, (h, m, s))  # convert these to int
            times.append(":".join([str(h), str(m), str(s)]))
            videos.append(name)
            flags.append(args)
            video_list.append(Video(h, m, s, name, args))
            # Enqueue videos for playing. If the video is set to play manually, do not enqueue.
            if h != -1:
                t = threading.Thread(target=lambda: scheduler.enqueue(Video(h, m, s, name, ["--fullscreen"])))
                t.start()
                # we need a list to keep track of these threads, so they can be stopped later if the video is deleted
        except IndexError:
            continue

    model = VideoTableModel(None, video_list, ["Video File Name", "Play Time", "Duration"])
    ui.table_videos.setModel(model)


# creates new video entry to be played in table
def select_video():
    global video
    video = QFileDialog.getOpenFileName()
    ui2.label_load_video_name.setText(video[0].split('/')[-1])


def inspect(new: bool):
    window2.show()
    global video
    ui2.buttonBox.disconnect()
    ui2.buttonBox.accepted.connect(window2.accept)
    ui2.buttonBox.rejected.connect(window2.reject)    
    ui2.buttonBox.accepted.connect(lambda: entry(new))
    print("run")
    

def entry(new: bool):
    if new:
        print("i'm new!")
    if video[0] != "":
        vst_file = open(location, "a")
        # print (video[0])
        # its currently hard coded to 8:06 PM, will add UI support
        print(ui2.hours.value())
        vst_file.write(" ".join([str(ui2.hours.value()), str(ui2.minutes.value()), str(ui2.seconds.value()), ""]) + video[0] + " none\n")
        vst_file.close()
        table_dump()

        # set the text to 
        ui.label_now_playing.setText(video[0].split('/')[-1])


def table_clicked(position):
    index = ui.table_videos.selectedIndexes()[0]
    menu = QMenu()
    actionInspect = menu.addAction("Inspect")
    actionDelete = menu.addAction("Delete")
    # actionDelete.setEnabled(False)
    menu.exec_(ui.table_videos.viewport().mapToGlobal(position))
# opens gui window


# Initialize the GUI interface (put widgets and windows on the actual screen where humans can see them)    
def main():
    global app
    app = QApplication(sys.argv)

    global window2
    global window3
    global credits_window

    window = QMainWindow()
    window2 = QDialog()
    window3 = QDialog()
    credits_window = QDialog()

    global ui
    global ui2
    global ui3
    global credits_ui

    ui = MainUI()
    ui.setupUi(window)

    model = VideoTableModel(None, [], ["Video File Name", "Play Time", "Duration"])
    ui.table_videos.setSelectionMode(QAbstractItemView.SingleSelection)
    ui.table_videos.setSelectionBehavior(QAbstractItemView.SelectRows)
    ui.table_videos.setModel(model)
    ui.table_videos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    # ui.table_videos.clicked.connect(table_clicked)
    ui.table_videos.setContextMenuPolicy(Qt.CustomContextMenu)
    ui.table_videos.customContextMenuRequested.connect(table_clicked)
    ui2 = LoadVideoDialog()
    ui2.setupUi(window2)

    ui3 = NothingToInspectDialog()
    ui3.setupUi(window3)

    bind()
    # ui.table_videos.setRowCount(0)
    # window.setWindowTitle("Video Scheduling Utility by KVK")
    window.show()
    open_vst()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
