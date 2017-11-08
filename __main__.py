#!/usr/bin/python3
# Import PyQt5. If it's not installed, try to install it.
import os
import platform
import subprocess
import sys

try:
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QAbstractItemView, QHeaderView, QMenu
except ImportError:
    print("Installing dependencies...")
    subprocess.Popen(['pip3', 'install', 'PyQt5'])

from ui.generated.load_video_dialog import Ui_Dialog as LoadVideoDialog
from ui.generated.nothing_to_inspect import Ui_Dialog as NothingToInspectDialog
from ui.generated.main_window import Ui_MainWindow as MainUI
from video import Video
# binds all buttons to functions
from video_table_model import VideoTableModel
from ui.generated.vst_prefs import Ui_Dialog as prefs


def bind():
    # Connect Main UI Load New button to Load New function
    # Inspector OK button bindings moved to inspector due to design limitations and human idiocy
    ui.inspector.clicked.connect(lambda: inspect(False))
    ui.loadnew.clicked.connect(lambda: inspect(True))
    ui2.button_choose_video.clicked.connect(select_video)
    ui.actionQuit.triggered.connect(app.quit)
    ui.actionSettings.triggered.connect(prefshow)
    # ui.actionAbout.triggered.connect(credits_window.exec_)
    ui.actionHelp.triggered.connect(show_help)
    ui.actionAbout.triggered.connect(show_help)


def prefshow():
    prefs_window.show()
    prefs_ui.helpabout.hide()
    prefs_ui.output.hide()
    prefs_ui.person.show()


def show_help():
    prefs_window.show()
    prefs_ui.output.hide()
    prefs_ui.person.hide()
    prefs_ui.helpabout.show()


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


def get_length(filename):
    result = subprocess.run(["ffprobe", filename],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return \
    [x for x in result.stdout.decode('utf-8').splitlines() if "Duration" in x][0].split()[1].split(",")[0].split(".")[0]


# Dump all entries into a QTable for editing in the GUI
def table_dump():
    with open(location) as f:
        table = f.read().splitlines()
    print(table)
    # Change rows to amount of "queued" videos
    video_list = []
    times = []
    videos = []
    flags = []

    for row in table:
        try:
            h, m, s, name, args = row.split(',')  # to be safe(and readable), always put the ' '
            h, m, s = map(int, (h, m, s))  # convert these to int
            print(name)
            length = get_length(name)
            print(length)
            times.append(":".join([str(h), str(m), str(s)]))
            videos.append(name)
            flags.append(args)
            # make sure video uses os-specific directory separator
            print("Not removed", name)
            name = name.replace("C:/", "")
            print("Removed", name)
            name_split = name.split("/")
            print("System: ", platform.system())
            if platform.system() == "Windows":
                print("Windows!")
                name_split.insert(0, "C:\\")
            print(name_split)
            name = os.path.join(*name_split)
            print("Name:", name)
            if platform.system() == "Linux":
                name = "/" + name
            if h != -1:
                video_list.append(Video(h, m, s, name, [], length, True))
            else:
                video_list.append(Video(h, m, s, name, [], length, False))
                # print("Video list:", video_list)

                # Enqueue videos for playing. If the video is set to play manually, do not enqueue.
                # we need a list to keep track of these threads, so they can be stopped later if the video is deleted
        except (IndexError, ValueError):
            continue

    print("Video list:", video_list)
    model = VideoTableModel(None, video_list, ["Video File Name", "Play Time", "Duration"])
    ui.table_videos.setModel(model)


# creates new video entry to be played in table
def select_video():
    global video
    video = QFileDialog.getOpenFileName()
    ui2.label_load_video_name.setText(video[0].split('/')[-1])
    ui2.label_load_video_length.setText(get_length(video[0]))


def inspect(new: bool):
    inspected_row = 0
    show = True
    if not new:
        print("im old")
        if not len(ui.table_videos.selectionModel().selectedRows()) > 0:
            window3.show()
            show = False
        else:
            # Get selected row
            global video
            print("inspecting")
            inspected_row = ui.table_videos.selectionModel().selectedRows()[0].row()
            ui2.label_load_video_name.setText(ui.table_videos.model().data[inspected_row].filename.split('/')[-1])
            print("setting video var")
            video = [ui.table_videos.model().data[inspected_row].filename, "Never Gonna Give You Up"]
            print(video)

            # Set inspector values to values in inspected row
            ui2.hours.setValue(int(ui.table_videos.model().data[inspected_row].hour))
            ui2.minutes.setValue(int(ui.table_videos.model().data[inspected_row].minute))
            ui2.seconds.setValue(int(ui.table_videos.model().data[inspected_row].second))

    if show:
        window2.show()
        ui2.buttonBox.disconnect()
        ui2.buttonBox.accepted.connect(window2.accept)
        ui2.buttonBox.rejected.connect(window2.reject)
        ui2.buttonBox.accepted.connect(lambda: entry(new, inspected_row))
        print("run")


def entry(new: bool, inspected_row: int):
    vst_file = open(location, "a+")
    print(video)
    if new:
        print("i'm new!")
    try:
        if video[0] != "":

            if ui2.manualPlay.checkState():
                if not new:
                    print("YEE")
                    vst_file.seek(0, 0)  # reset file pointer to beginning
                    entries = vst_file.readlines()  # read lines from file

                    del entries[inspected_row]
                    entries.insert(inspected_row, "-1,-1,-1," + video[0] + ",none\n")  # replace line

                    vst_file.seek(0, 0)  # reset again because file was just parsed
                    vst_file.truncate()
                    vst_file.write("".join(entries))
                    vst_file.close()
                else:

                    vst_file.write("-1,-1,-1," + video[0] + ",none\n")
                    vst_file.close()

            else:
                if not new:
                    vst_file.seek(0, 0)  # reset file pointer to beginning
                    entries = vst_file.readlines()  # read lines from file

                    del entries[inspected_row]
                    entries.insert(inspected_row, ",".join(
                        [str(ui2.hours.value()), str(ui2.minutes.value()), str(ui2.seconds.value()), ""]) + video[
                                       0] + ",none\n")  # replace line
                    vst_file.seek(0, 0)  # reset again because file was just parsed
                    vst_file.truncate()
                    vst_file.write("".join(entries))

                    vst_file.close()
                else:

                    vst_file.write(
                        ",".join([str(ui2.hours.value()), str(ui2.minutes.value()), str(ui2.seconds.value()), ""]) +
                        video[0] + ",none\n")
                    vst_file.close()

            vst_file.close()
            table_dump()
            ui.label_now_playing.setText(video[0].split('/')[-1])
    except:
        pass

        # set the text to


def table_right_clicked(position):
    index = ui.table_videos.selectedIndexes()[0]
    menu = QMenu()
    action_inspect = menu.addAction("Inspect")
    action_delete = menu.addAction("Delete")
    action_delete.setEnabled(False)

    action_inspect.triggered.connect(lambda: inspect(False))
    menu.exec_(ui.table_videos.viewport().mapToGlobal(position))


def table_double_clicked(index):
    if index.column() == 0:
        # we want to open a file dialog to choose new video
        filename, status = QFileDialog.getOpenFileName(caption="Choose Video File")
        print(filename)
    else:
        return


# opens gui window


# Initialize the GUI interface (put widgets and windows on the actual screen where humans can see them)
def main():
    global app
    app = QApplication(sys.argv)
    global window2
    global window3
    global credits_window
    global prefs_window

    window = QMainWindow()
    window2 = QDialog()
    window3 = QDialog()
    credits_window = QDialog()
    prefs_window = QDialog()

    global ui
    global ui2
    global ui3
    global credits_ui
    global prefs_ui

    ui = MainUI()
    ui.setupUi(window)

    model = VideoTableModel(None, [], ["Video File Name", "Play Time", "Duration"])
    ui.table_videos.setSelectionMode(QAbstractItemView.SingleSelection)
    ui.table_videos.setSelectionBehavior(QAbstractItemView.SelectRows)
    ui.table_videos.setModel(model)
    ui.table_videos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    # ui.table_videos.clicked.connect(table_clicked)
    ui.table_videos.setContextMenuPolicy(Qt.CustomContextMenu)
    ui.table_videos.customContextMenuRequested.connect(table_right_clicked)
    ui.table_videos.doubleClicked.connect(table_double_clicked)
    ui.actionSettings.triggered.connect(prefs_window.show)

    ui2 = LoadVideoDialog()
    ui2.setupUi(window2)

    ui3 = NothingToInspectDialog()
    ui3.setupUi(window3)

    prefs_ui = prefs()
    prefs_ui.setupUi(prefs_window)

    bind()
    # ui.table_videos.setRowCount(0)
    # window.setWindowTitle("Video Scheduling Utility by KVK")
    window.show()
    open_vst()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
