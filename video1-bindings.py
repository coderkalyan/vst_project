#!/usr/bin/python3
import sys
<<<<<<< HEAD
=======
import scheduler
from video import Video
>>>>>>> d9bf78e821626ea86d8b719b1e7be7804db44060
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QFileDialog, QLabel
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtGui, QtCore
from video1 import Ui_MainWindow as videosched
from load_video_dialog import Ui_Dialog as videodialog
from nothing_to_inspect import Ui_Dialog as nothing_to_inspect

#binds all buttons to functions

def bind():
    ui.loadnew.clicked.connect(newEntry)

def vidNamer(video):
    dev = ""
    for i in range(len(video)):
        dev = video
        for i2 in range(len(dev)):
            try:
                if dev[i2] == '/':
                    dev = dev[i2+1:len(dev)]
                    print(dev)
            except IndexError:
                break
            ui.label.setText("Playing: " + dev)
<<<<<<< HEAD
=======
            return dev
>>>>>>> d9bf78e821626ea86d8b719b1e7be7804db44060

#---------------------------------------------------------------------
            
def openvst():
    #opens a text file for reading and writing video entries
    
    try:
        vst = open("pointer.txt", "r")
        global location
        location = vst.read()
        vst.close()
        editvst()
    except FileNotFoundError:
        vst2 = open("pointer.txt", "w+")
        vst2.writelines("\nvstdefault.txt")
        vst2.close()
        openvst()            

def editvst():
    vst3 = open(location, "r")
    
    global table
    table = vst3.read()
   
    tableDump()
    vst3.close()
        
#---------------------------------
#Dump all entries into a QTable for editing in the GUI
def tableDump():
    splittable = table.splitlines()
    ui.schedtable.setRowCount(len(splittable))
    print(len(splittable))
    times = []
    videos = []
    flags = []
    for i in splittable:
        try:
            j = i.split()
            times.append(j[0]+":"+j[1]+":"+j[2])
            videos.append(j[3])
            flags.append(j[4])
<<<<<<< HEAD
=======
            print(j[0])
            if j[0] != "-1":
                scheduler.enqueue(Video(int(j[0]), int(j[1]), int(j[2]), j[3], ["--fullscreen"]))
            else:
                print ("ooh ya")
>>>>>>> d9bf78e821626ea86d8b719b1e7be7804db44060
        except IndexError:
            continue
    
    c=0
<<<<<<< HEAD
=======
    #------
    #Dump the vst's contents into the actual QTable
    print("I am running")
>>>>>>> d9bf78e821626ea86d8b719b1e7be7804db44060
    for k in times:
        
        if k != "-1:-1:-1":
            vidlabel = QLabel()
            vidlabel.setText(k)
            ui.schedtable.setCellWidget(c, 1, vidlabel)
        c=c+1
    c=0
    for m in videos:
        
        vidlabel2 = QLabel()
        vidlabel2.setText(m)
        ui.schedtable.setCellWidget(c, 0, vidlabel2)
        c=c+1
        
#---------------------------------------------------        
    



#creates new video entry to be played in table

def newEntry():
    video = QFileDialog.getOpenFileName()
    print(video)
    if video[0]!="":
        vstfile = open(location, "a")
        #print (video[0])
<<<<<<< HEAD
        vstfile.write("-1 -1 -1 " + video[0] + " none\n")
=======
        vstfile.write("20 6 0 " + video[0] + " none\n")
>>>>>>> d9bf78e821626ea86d8b719b1e7be7804db44060
        vstfile.close()
        editvst()
        tableDump()
        vidNamer(video[0])
     
    
#opens gui window

    
def start():
    app = QApplication(sys.argv)
    
    global window2
    global window3
    
    window = QMainWindow()
    window2 = QDialog()
    window3 = QDialog()
    
    global ui
    global ui2
    global ui3
    
    ui = videosched()
    ui.setupUi(window)
    
    ui2 = videodialog()
    ui2.setupUi(window2)
    
    ui3 = nothing_to_inspect()
    ui3.setupUi(window3)
    
    bind()
    ui.schedtable.setRowCount(0)
    window.setWindowTitle("Video Scheduling Utility by KVK")
    window.show()    
    openvst()    
    sys.exit(app.exec_())
    
#executes start
    
if __name__ == "__main__":
    start()
