import socket
import sys
import threading
import time
from tkinter import *


def port_scan_clear():
    listbox.delete(0, 'end')


def txt_clear():
    file = open("results.txt", "w").close()


def scan_to_txt(x):
    file = open("results.txt", "a")
    file.write(x + "\n")


def port_scan_info(ip, prt):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
            if sckt.connect_ex((ip, prt)) == 0:
                service_name = socket.getservbyport(prt, "tcp")
                x = "Port %d  open, %s" % (prt, service_name)
                scan_to_txt(x)
                listbox.insert("end", str(x))

    except OSError:
        print("ERROR")
    except:
        sckt.close()
        sys.exit()
    sys.exit()


def port_scan():
    port_scan_clear()
    txt_clear()

    start_val = int(box1.get())
    end_val = int(box2.get())

    try:
        ip = socket.gethostbyname(str(box.get()))
        ip = str(box.get())
        while start_val <= end_val:
            try:
                start_scan = threading.Thread(target=port_scan_info, args=(ip, start_val))
                start_scan.setDaemon(True)
                start_scan.start()

            except:
                time.sleep(0.01)
            start_val += 1
    except:
        err = "Error, " + str(box.get())
        print(err)
        listbox.insert(0, str(err))


# UI ----------------------------


ui = Tk()
ui.title("Port scanner")
# COLOURS ----------
col1 = "#FFFFFF"
col2 = "#222222"
col3 = "#000000"
col4 = "#111111"
# ------------
ui.tk_setPalette(background=col2, foreground=col1, activeBackground=col4,
                 activeForeground=col3, highlistColor=col1, highlight=col1)
txt1 = Label(ui, text="Enter IP address or website")
txt1.pack(fill=X)
box = Entry(ui, width=60)
box.insert(0, "127.0.0.1")
box.pack(fill=X)

txt2 = Label(ui, text="Enter starting port")
txt2.pack()

box1 = Entry(ui, width=60, text="1")
box1.insert(0, "1")
box1.pack(fill=X)

txt3 = Label(ui, text="Enter end port")
txt3.pack(fill=X)

box2 = Entry(ui, width=60)
box2.insert(0, "1000")
box2.pack(fill=X)

# FRAME------------
frame = LabelFrame(ui)
scroll = Scrollbar(frame, orient=VERTICAL)

listbox = Listbox(frame, width=60, yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
frame.pack(fill=X)
listbox.pack(fill=X)

# ----------------
button1 = Button(ui, text="start", command=port_scan)
button1.pack()

# ------------------------------------

ui.mainloop()
