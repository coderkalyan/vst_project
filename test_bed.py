#!/usr/bin/python3
import sys
import subprocess
# Import PyQt5. If it's not installed, try to install it.
import os
import platform
import configparser

from schedule_saver import DBManager, Schedule

try:
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QAbstractItemView, QHeaderView, QMenu
except ImportError:
    print("Installing dependencies...")
    subprocess.Popen(['pip3', 'install', 'PyQt5'])

import scheduler
from ui.generated.load_video_dialog import Ui_Dialog as LoadVideoDialog
from ui.generated.nothing_to_inspect import Ui_Dialog as NothingToInspectDialog
from ui.generated.main_window import Ui_MainWindow as MainUI
from video import Video
# binds all buttons to functions
from video_table_model import VideoTableModel
from ui.generated.vst_prefs import Ui_Dialog as prefs
import test_bed3

VSTX_SAVE = 1
VST_SAVE = 2


class VideoGUI():
    def __init__(self):
        self.FFPROBE_PATH = "ffprobe"
        app = QApplication(sys.argv)

        window = QMainWindow()
        window2 = QDialog()
        window3 = QDialog()
        credits_window = QDialog()
        prefs_window = QDialog()

        ui = MainUI()
        ui.setupUi(window)

        model = VideoTableModel(None, [], ["Video File Name", "Play Time", "Duration"])
        ui.table_videos.setSelectionMode(QAbstractItemView.SingleSelection)
        ui.table_videos.setSelectionBehavior(QAbstractItemView.SelectRows)
        ui.table_videos.setModel(model)
        ui.table_videos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        # ui.table_videos.clicked.connect(table_clicked)
        ui.table_videos.setContextMenuPolicy(Qt.CustomContextMenu)
        ui.table_videos.customContextMenuRequested.connect(self.table_right_clicked)
        ui.table_videos.doubleClicked.connect(self.table_double_clicked)
        ui.actionSettings.triggered.connect(prefs_window.show)

        ui2 = LoadVideoDialog()
        ui2.setupUi(window2)

        ui3 = NothingToInspectDialog()
        ui3.setupUi(window3)

        prefs_ui = prefs()
        prefs_ui.setupUi(prefs_window)

        self.ui = ui
        self.ui2 = ui2
        self.ui3 = ui3
        self.prefs_ui = prefs_ui

        self.window = window
        self.window2 = window2
        self.window3 = window3
        self.credits_window = credits_window
        self.prefs_window = prefs_window

        self.app = app

        print("i am dying inside")

        self.bind()
        # ui.table_videos.setRowCount(0)
        # window.setWindowTitle("Video Scheduling Utility by KVK")
        self.window.show()
        self.open_vst()
        sys.exit(app.exec_())

    def bind(self):
        # Connect Main UI Load New button to Load New function
        # Inspector OK button bindings moved to inspector due to design limitations and human idiocy
        self.ui.inspector.clicked.connect(lambda: self.inspect(False))
        self.ui.loadnew.clicked.connect(lambda: self.inspect(True))
        self.ui2.button_choose_video.clicked.connect(self.select_video)
        self.prefs_ui.savebutton.clicked.connect(self.save_prefs)

        self.ui.actionQuit.triggered.connect(self.app.quit)
        self.ui.actionSettings.triggered.connect(self.pref_show)
        # ui.actionAbout.triggered.connect( .exec_)
        self.ui.actionHelp.triggered.connect(help)
        self.ui.actionAbout.triggered.connect(help)

    def save_prefs(self):
        config = configparser.ConfigParser()
        config['PLAYER'] = {'ffprobe': self.FFPROBE_PATH,
                             'player': 'mplayer',
                             'player-path': 'mplayer'}
        config['GUI'] = {'theme': 'material-design',
                         'minimal': False,
                         'large-buttons': False}
        with open('config.ini', 'w+') as configfile:
            config.write(configfile)

    def pref_show(self):
        self.prefs_window.show()
        self.prefs_ui.helpabout.hide()
        self.prefs_ui.output.hide()
        self.prefs_ui.person.show()

    def help(self):
        self.prefs_window.show()
        self.prefs_ui.output.hide()
        self.prefs_ui.person.hide()
        self.prefs_ui.helpabout.show()

    def open_vst(self):
        # opens a text file for reading and writing video entries

        with open("pointer.txt", "w+") as pointer:
            self.location = pointer.read()
            # if we read from empty file(just created), fill it with path to default table
            if self.location == "":
                self.location = "vstdefault.txt"
                pointer.write(self.location)
        self.table_dump()

    @staticmethod
    def get_length(filename):
        try:
            result = subprocess.run(["ffprobe", filename],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            return \
                [x for x in result.stdout.decode('utf-8').splitlines() if "Duration" in x][0].split()[1].split(",")[
                    0].split(".")[0]
        except FileNotFoundError:
            return

    # Dump all entries into a QTable for editing in the GUI
    def table_dump(self):
        try:
            # with open(self.location) as f:
            #    self.table = f.read().splitlines()
            with DBManager("schedules.vstx") as conn:
                # TODO: multiple schedules
                # TODO: use configs from preferences or drop down
                schedule = Schedule(conn)
                print("write1")
                ## TODO: remove the following 3 lines - just for debug
                table = schedule.list_all()
                print(table, "listall")

        except FileNotFoundError:
            f2 = open(self.location, "w+")
            f2.close()
            table = []
            self.table_dump()
        # Change rows to amount of "queued" videos
        self.video_list = []
        times = []
        videos = []
        flags = []
        print(table,"table")

        for row in table:
            print(row.filename, "row")
            try:
                # h, m, s, name, args = row  # row.split(',')
                h, m, s, name, args = row.hour, row.minute, row.second, row.filename, row.flags
                print(h,m,s,name,args,"YEEE")
                print("Phase 1")
                # h, m, s = map(int, (h, m, s))  # convert these to int
                print(name, "name")
                length = self.get_length(name)
                print(length, "length")
                print(h, m, s)
                # times.append(":".join([str(h), str(m), str(s)]))
                # videos.append(name)
                # flags.append(args)

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
                # if h != -1:
                video = Video(h, m, s, name, ["--fullscreen"], length, h != -1)
                print(video.filename, "filenaame")
                self.video_list.append(video)
                print(self.video_list, "vidlist")
                print("wtf this should be working")                 
                print("wrote to db")
                # else:
                    # self.video_list.append(Video(h, m, s, name, ["--fullscreen"], length, False))
                    # print("Video list:", self.video_list)

                    # Enqueue videos for playing. If the video is set to play manually, do not enqueue.
                    # we need a list to keep track of these threads, so they can be stopped later
                    # if the video is deleted
                print(times, videos, flags, "total")
            except (IndexError, ValueError) as e:
                print(e)
                print(row, "row-except")
                print("excepted")
                continue
                     

        print("Video list:", self.video_list)
        model = VideoTableModel(None, self.video_list, ["Video File Name", "Play Time", "Duration"])
        self.ui.table_videos.setModel(model)

    # creates new video entry to be played in table
    def select_video(self):
        self.video = QFileDialog.getOpenFileName()
        self.ui2.label_load_video_name.setText(self.video[0].split('/')[-1])
        self.ui2.label_load_video_length.setText(self.get_length(self.video[0]))

    def inspect(self, new: bool):
        inspected_row = 0
        show = True
        if not new:
            print("im old")
            if not len(self.ui.table_videos.selectionModel().selectedRows()) > 0:
                self.window3.show()
                show = False
            else:
                # Get selected row
                inspected_row = self.ui.table_videos.selectionModel().selectedRows()[0].row()
                self.ui2.label_load_video_name.setText(self.ui.table_videos.model().data[inspected_row].filename.split('/')[-1])
                self.video = [self.ui.table_videos.model().data[inspected_row].filename, "Never Gonna Give You Up"]

                # Set inspector values to values in inspected row
                self.ui2.hours.setValue(int(self.ui.table_videos.model().data[inspected_row].hour))
                self.ui2.minutes.setValue(int(self.ui.table_videos.model().data[inspected_row].minute))
                self.ui2.seconds.setValue(int(self.ui.table_videos.model().data[inspected_row].second))

        if show:
            self.window2.show()
            self.ui2.buttonBox.disconnect()
            self.ui2.buttonBox.accepted.connect(self.window2.accept)
            self.ui2.buttonBox.rejected.connect(self.window2.reject)
            self.ui2.buttonBox.accepted.connect(lambda: self.entry(new, inspected_row, VSTX_SAVE))
            print("run")

    def entry(self, new: bool, inspected_row: int, savetype: int):
        if new:
            print("i'm new!")
        try:
            # TODO: replace hotfix so that objects can be deleted without issues
            if savetype == 1:
                print(self.video_list)
                if self.video[0] != "":
                    if self.ui2.manualPlay.checkState():
                        print("i need help")
                        if not new:
                            with DBManager("schedules.vstx") as conn:
                                schedule = Schedule(conn)
                                print(self.video_list, "listtt")
                                print(self.video_list[inspected_row].id)
                                schedule.update(
                                    Video(
                                        -1,
                                        -1,
                                        -1,
                                        self.video[0],
                                        ["--fullscreen"],
                                        "1:00",
                                        False,
                                        inspected_row+1))
                        else:
                            with DBManager("schedules.vstx") as conn:
                                schedule = Schedule(conn)
                                schedule.insert(Video(-1, -1, -1, self.video[0], ["--fullscreen"], "1:00", False))
                    else:
                        print("my brain")
                        if not new:
                            with DBManager("schedules.vstx") as conn:
                                print(self.video_list, "listtt")
                                schedule = Schedule(conn)
                                print(self.video_list[inspected_row].id, "ID")
                                schedule.update(
                                    Video(
                                        self.ui2.hours.value(),
                                        self.ui2.minutes.value(),
                                        self.ui2.seconds.value(),
                                        self.video[0],
                                        ["--fullscreen"],
                                        "1:00",
                                        False,
                                        inspected_row+1))
                        else:
                            with DBManager("schedules.vstx") as conn:
                                print("WIEHGEIO")
                                print(self.ui2.hours.value(), self.ui2.minutes.value(), self.ui2.seconds.value())
                                hour, minute, second = self.ui2.hours.value(), self.ui2.minutes.value(), self.ui2.seconds.value()
                                schedule = Schedule(conn)
                                print("hoo")
                                schedule.insert(
                                    Video(hour,
                                          minute,
                                          second,
                                          self.video[0],
                                          ["--fullscreen"],
                                          "1:00",
                                          False))
                                # test_bed3.i_need_help(hour,minute,second,self.video[0],["--fullscreen"],"1:00",False)
                                print("done")
                    self.table_dump()
            elif savetype == 2:
                vst_file = open(self.location, "a+")
                print(self.video[0] + ": video name")
                if self.video[0] != "":
                    print(self.video, "phase 5")
                    print("setvar")

                    if self.ui2.manualPlay.checkState():
                        if not new:
                            print("YEE")
                            vst_file.seek(0, 0)  # reset file pointer to beginning
                            entries = vst_file.readlines()  # read lines from file

                            del entries[inspected_row]
                            entries.insert(inspected_row, "-1,-1,-1," + self.video[0] + ",none\n")  # replace line
                            print(entries)
                            vst_file.seek(0, 0)  # reset again because file was just parsed
                            vst_file.truncate()
                            vst_file.write("".join(entries))
                            vst_file.close()
                        else:

                            vst_file.write("-1,-1,-1," + self.video[0] + ",none\n")
                            vst_file.close()

                    else:
                        if not new:
                            print("wee")
                            vst_file.seek(0, 0)  # reset file pointer to beginning
                            entries = vst_file.readlines()  # read lines from file
                            print(inspected_row)
                            print("still running?")
                            print(entries, ": read lines")
                            del entries[inspected_row]
                            entries.insert(inspected_row, ",".join(
                                [str(self.ui2.hours.value()), str(self.ui2.minutes.value()), str(self.ui2.seconds.value()),
                                 ""]) + self.video[
                                               0] + ",none\n")  # replace line
                            print(entries, " printed entries")
                            vst_file.seek(0, 0)  # reset again because file was just parsed
                            vst_file.truncate()
                            vst_file.write("".join(entries))
                            print(vst_file.read(), " written entries?")

                            vst_file.close()
                        else:

                            vst_file.write(
                                ",".join([str(self.ui2.hours.value()), str(self.ui2.minutes.value()),
                                          str(self.ui2.seconds.value()), ""]) +
                                self.video[0] + ",none\n")
                            vst_file.close()

                    vst_file.close()
                    self.table_dump()
                    self.ui.label_now_playing.setText(self.video[0].split('/')[-1])
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

            # set the text to

    def table_right_clicked(self, position):
        index = self.ui.table_videos.selectedIndexes()[0]
        menu = QMenu()
        action_inspect = menu.addAction("Inspect")
        action_delete = menu.addAction("Delete")
        action_delete.setEnabled(False)

        def wrapper():
            self.inspect(False)

        action_inspect.triggered.connect(wrapper)
        menu.exec_(self.ui.table_videos.viewport().mapToGlobal(position))

    @staticmethod
    def table_double_clicked(index):
        if index.column() == 0:
            # we want to open a file dialog to choose new video
            filename, status = QFileDialog.getOpenFileName(caption="Choose Video File")
            print(filename)
        else:
            return


if __name__ == "__main__":
    VideoGUI()
