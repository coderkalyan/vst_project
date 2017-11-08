from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QMenu, QFileDialog, QDialog

from ui.generated.main_window_generated import Ui_MainWindow
from ui.load_video_dialog import LoadVideoDialog
from video_table_model import VideoTableModel


class MainUI(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)

        self.model = VideoTableModel(None, [], ["Video File Name", "Play Time", "Duration"])
        self.setup_table_videos()

        # TODO - implement play next
        self.next.setEnabled(False)

        self.inspector_dialog = QDialog(parent=window, flags=Qt.Dialog)
        self.inspector_dialog_ui = LoadVideoDialog(self.inspector_dialog)
        self.inspector_dialog_ui.setupUi(self.inspector_dialog)

    def setup_table_videos(self):
        self.table_videos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_videos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_videos.setModel(self.model)
        self.table_videos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_videos.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_videos.customContextMenuRequested.connect(self.table_right_clicked)
        self.table_videos.doubleClicked.connect(self.table_double_clicked)

    def table_right_clicked(self, position):

        index = self.table_videos.selectedIndexes()[0]
        menu = QMenu()
        action_inspect = menu.addAction("Inspect")
        action_delete = menu.addAction("Delete")
        action_delete.setEnabled(False)

        action_inspect.triggered.connect(lambda: self.inspect(False))
        menu.exec_(self.table_videos.viewport().mapToGlobal(position))

    def inspect(self, new: bool):
        pass
        inspected_row = 0
        show = True
        if not new:
            if not len(self.table_videos.selectionModel().selectedRows()) > 0:
                # TODO - show nothing to inspect dialog
                # window3.show()
                show = False
            else:
                # Get selected row
                inspected_row = self.table_videos.selectionModel().selectedRows()[0].row()
                self.inspector_dialog_ui.label_load_video_name.setText(
                    self.table_videos.model().data[inspected_row].filename.split('/')[-1])
                video = [self.table_videos.model().data[inspected_row].filename,
                         "Never Gonna Give You Up"]

                # Set inspector values to values in inspected row
                self.inspector_dialog_ui.hours.setValue(int(self.table_videos.model()
                                                            .data[inspected_row].hour))
                self.inspector_dialog_ui.minutes.setValue(int(self.table_videos.model()
                                                              .data[inspected_row].minute))
                self.inspector_dialog_ui.seconds.setValue(int(self.table_videos.model()
                                                              .data[inspected_row].second))

        if show:
            self.inspector_dialog.show()
            self.inspector_dialog_ui.buttonBox.disconnect()
            self.inspector_dialog_ui.buttonBox.accepted.connect(self.inspector_dialog.accept)
            self.inspector_dialog_ui.buttonBox.rejected.connect(self.inspector_dialog.reject)
            self.inspector_dialog_ui.buttonBox.accepted.connect(lambda: entry(new, inspected_row))
            print("run")

    def table_double_clicked(self, index):
        # TODO - actually change filename
        if index.column() == 0:
            # we want to open a file dialog to choose new video
            filename, status = QFileDialog.getOpenFileName(caption="Choose Video File")
            print(filename)
        else:
            return

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
                        entries.insert(inspected_row,
                                       "-1,-1,-1," + video[0] + ",none\n")  # replace line

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
                            [str(ui2.hours.value()), str(ui2.minutes.value()),
                             str(ui2.seconds.value()), ""]) + video[
                                           0] + ",none\n")  # replace line
                        vst_file.seek(0, 0)  # reset again because file was just parsed
                        vst_file.truncate()
                        vst_file.write("".join(entries))

                        vst_file.close()
                    else:

                        vst_file.write(
                            ",".join([str(ui2.hours.value()), str(ui2.minutes.value()),
                                      str(ui2.seconds.value()), ""]) +
                            video[0] + ",none\n")
                        vst_file.close()

                vst_file.close()
                table_dump()
                ui.label_now_playing.setText(video[0].split('/')[-1])
        except:
            pass

            # set the text to
