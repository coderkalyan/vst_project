def openvst():
    
    def editvst():
        vst3 = open(location, "r")
        
        global table
        table = vst3.read()
        
        tableDump()
    def tableDump():
        splittable = table.splitlines()
        
        times = []
        videos = []
        flags = []
        for i in splittable:
            j = i.split()
            
            times.append(j[0]+":"+j[1]+":"+j[2])
            videos.append(j[3])
            flags.append(j[4])
        
        for k in times:
            vidlabel = QLabel().setText(k)
            ui.schedtable.setCellWidget(ui.schedtable.rowCount(), 0, vidlabel)
        for m in videos:
            vidlabel2 = QLabel().setText(m)
            ui.schedtable.setCellWidget(ui.schedtable.rowCount(), 0, vidlabel2)
        
    try:
        vst = open("pointer.txt", "r")
        location = vst.read()
        vst.close()
        editvst()
    except FileNotFoundError:
        vst2 = open("pointer.txt", "w+")
        vst2.write("vstdefault.txt")
        vst2.close()
        openvst()
openvst()
