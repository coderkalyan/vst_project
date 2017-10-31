#!/usr/bin/python3
# Tested version with fixed indents and a few  big fixes in table_dump()
import sys
import threading

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QLabel

import scheduler
from load_video_dialog import Ui_Dialog as VideoDialog
from nothing_to_inspect import Ui_Dialog as NothingToInspectDialog
from video import Video
from video1 import Ui_MainWindow as MainUI


# binds all buttons to functions
def bind():
    ui.loadnew.clicked.connect(new_entry)
    ui.actionQuit.triggered.connect(app.quit)


def open_vst():
    # opens a text file for reading and writing video entries
    global location

    with open("pointer.txt", "r+") as pointer:
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
    ui.table_videos.setRowCount(len(table))
    print(len(table))
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

            # Enqueue videos for playing. If the video is set to play manually, do not enqueue.
            print(h)
            if h != -1:
                t = threading.Thread(target=lambda: scheduler.enqueue(Video(h, m, s, name, ["--fullscreen"])))
                t.start()
                # we need a list to keep track of these threads, so they can be stopped later if the video is deleted
        except IndexError:
            continue

    # loop through both lists at same time - videos -> video, times -> time, and keep the index -> i
    for i, (video, time) in enumerate(zip(videos, times)):
        label = QLabel()
        label.setText(video)
        ui.table_videos.setCellWidget(i, 0, label)
        label = QLabel()
        # basically set the time if it isn't -1, else set to 'manual'
        label.setText(time if time != "-1:-1:-1" else "Manual Play")
        ui.table_videos.setCellWidget(i, 1, label)


# creates new video entry to be played in table

def new_entry():
    video = QFileDialog.getOpenFileName()
    print(video)
    if video[0] != "":
        vstfile = open(location, "a")
        # print (video[0])
        # its currently hard coded to 8:06 PM, will add UI support
        vstfile.write("-1 -1 -1 " + video[0] + " none\n")
        vstfile.close()
        table_dump()

        # set the text to
        ui.label_now_playing.setText(video[0].split('/')[-1])


# opens gui window

# Initialize the GUI interface (put widgets and windows on the actual screen where humans can see them)
def main():
    global app

    app = QApplication(sys.argv)

    # global window2
    global window3

    window = QMainWindow()
    window2 = QDialog()
    window3 = QDialog()

    global ui
    global ui2
    global ui3

    ui = MainUI()
    ui.setupUi(window)

    ui2 = VideoDialog()
    ui2.setupUi(window2)

    ui3 = NothingToInspectDialog()
    ui3.setupUi(window3)

    bind()
    window.show()
    open_vst()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()