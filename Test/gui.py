# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
import socket
import time
import threading

from queue import Queue

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        #setting the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(550,300,800, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle(_translate("MainWindow", "Port Scanner"))

        #********************************************************
        #Ip Form
        #********************************************************

        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setGeometry(QtCore.QRect(10, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ip_label.setFont(font)
        self.ip_label.setText(_translate("MainWindow", "What is the IP address?"))

        self.input_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ip.setGeometry(QtCore.QRect(20, 50, 181, 31))

        #********************************************************
        #Port Range Form
        #********************************************************

        self.ports_label = QtWidgets.QLabel(self.centralwidget)
        self.ports_label.setGeometry(QtCore.QRect(10, 90, 281, 81))
        self.ports_label.setFont(font)
        self.ports_label.setText(_translate("MainWindow", "What is the range of ports?"))

        self.warning_ports = QtWidgets.QLabel(self.centralwidget)
        self.warning_ports.setGeometry(QtCore.QRect(20, 150, 371, 21))
        font.setPointSize(13)
        self.warning_ports.setFont(font)
        self.warning_ports.setText(_translate("MainWindow", "If no ports specified, scan the first "))
        self.warning2_ports = QtWidgets.QLabel(self.centralwidget)
        self.warning2_ports.setGeometry(QtCore.QRect(20, 160, 101, 41))
        self.warning2_ports.setFont(font)
        self.warning2_ports.setText(_translate("MainWindow", "1024 ports."))

        self.input_ports = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ports.setGeometry(QtCore.QRect(20, 200, 181, 31))

        #*********************************************************
        #Speed Form
        #*********************************************************

        self.speed_label = QtWidgets.QLabel(self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(330, 10, 461, 41))
        font.setPointSize(17)
        self.speed_label.setFont(font)
        self.speed_label.setText(_translate("MainWindow", "How fast would you want the scan to be?"))

        self.speed_warning_label = QtWidgets.QLabel(self.centralwidget)
        self.speed_warning_label.setGeometry(QtCore.QRect(340, 40, 411, 41))
        font.setPointSize(13)
        self.speed_warning_label.setFont(font)
        self.speed_warning_label.setText(_translate("MainWindow", "Please check only one box. If none of them is checked "))
        self.speed_warning2_label = QtWidgets.QLabel(self.centralwidget)
        self.speed_warning2_label.setGeometry(QtCore.QRect(340, 70, 421, 21))
        self.speed_warning2_label.setFont(font)
        self.speed_warning2_label.setText(_translate("MainWindow", "or more than one are checked, go with default ( Medium)."))

        #CheckBoxes
        self.checkBox_fastest = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_fastest.setGeometry(QtCore.QRect(330, 100, 331, 25))
        font.setPointSize(14)
        self.checkBox_fastest.setFont(font)
        self.checkBox_fastest.setText(_translate("MainWindow", "The fastest, don\'t wait any second"))

        self.checkBox_fast = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_fast.setGeometry(QtCore.QRect(330, 140, 231, 25))
        self.checkBox_fast.setFont(font)
        self.checkBox_fast.setText(_translate("MainWindow", "Fast, wait just a bit"))

        self.checkBox_medium = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_medium.setGeometry(QtCore.QRect(330, 180, 261, 21))
        self.checkBox_medium.setFont(font)
        self.checkBox_medium.setText(_translate("MainWindow", "Medium, wait one second"))

        self.checkBox_slow = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_slow.setGeometry(QtCore.QRect(330, 220, 201, 25))
        self.checkBox_slow.setFont(font)
        self.checkBox_slow.setText(_translate("MainWindow", "Slow, wait 2 seconds"))

        self.checkBox_slowest = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_slowest.setGeometry(QtCore.QRect(330, 260, 271, 25))
        self.checkBox_slowest.setFont(font)
        self.checkBox_slowest.setText(_translate("MainWindow", "The slowest, wait 5 seconds"))

        #************************************************************
        #Output File Form
        #************************************************************

        self.output_file_label = QtWidgets.QLabel(self.centralwidget)
        self.output_file_label.setGeometry(QtCore.QRect(330, 290, 411, 101))
        font.setPointSize(17)
        self.output_file_label.setFont(font)
        self.output_file_label.setText(_translate("MainWindow", "Do you want to output the scan to a file?"))

        self.outfile_label = QtWidgets.QLabel(self.centralwidget)
        self.outfile_label.setGeometry(QtCore.QRect(340, 360, 291, 21))
        font.setPointSize(13)
        self.outfile_label.setFont(font)
        self.outfile_label.setText(_translate("MainWindow", "If yes, write the name of the file:"))

        self.input_outfile = QtWidgets.QLineEdit(self.centralwidget)
        self.input_outfile.setGeometry(QtCore.QRect(340, 390, 231, 31))

        self.outfile_label2 = QtWidgets.QLabel(self.centralwidget)
        self.outfile_label2.setGeometry(QtCore.QRect(340,410,461,50))
        self.outfile_label2.setFont(font)
        self.outfile_label2.setText(_translate("MainWindow", "(You will still see the scanning, but it's saving at the end)"))

        #***********************************************************
        #Submit Button
        #***********************************************************

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(170, 370, 131, 61))
        self.button.setText(_translate("MainWindow", "Start scanning"))


        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.button.clicked.connect(self.verifying)


    def verifying(self):
        #Verifying the IP address
        self.ip=self.input_ip.text()
        #Put your code here

        #Verifying the port range
        if (self.input_ports.text()==''):
            self.portmin=1
            self.portmax=1024
        else:
            ports=self.input_ports.text().split("-")
            if (len(ports)==2):
                self.portmin=int(ports[0])
                self.portmax=int(ports[1])
            else:
                self.portmin=1
                self.portmax=int(self.input_ports.text())
        
          
        #Verifying which checkbox is selected
        nr=0
        if (self.checkBox_fastest.isChecked()==1):
            self.v = 0.25
            nr += 1
        if (self.checkBox_fast.isChecked()==1):
            self.v = 1
            nr += 1
        if(self.checkBox_medium.isChecked()==1):
            self.v = 2
            nr += 1
        if(self.checkBox_slow.isChecked()==1):
            self.v = 5
            nr += 1
        if(self.checkBox_slowest.isChecked()==1):
            self.v = 10000000
            nr += 1

        if(nr==0 or nr>1):
            self.v = 1
        
        if(self.input_outfile.text()==''):
            pass
        else:
            filename=self.input_outfile.text()
            f = open(filename,"x")
        self.scanning()
        
        
    def scanning(self):
        socket.setdefaulttimeout(self.v)
        print_lock = threading.Lock()
        
        #try:
        t_IP = socket.gethostbyname(self.ip)
        print('Starting scan on host:', t_IP)
        #except socket.gaierror:
         #   msg = QtWidgets.QMessageBox()
          #  msg.setWindowTitle("Wrong IP address")
           # msg.setText("The host could not be resolved")


        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))
                with print_lock:
                    print("Port %s is open. Service name: %s" %(port,socket.getservbyport(port,"tcp")))

           # except socket.gaierror:
            #    msg = QtWidgets.QMessageBox()
             #   msg.setWindowTitle("Wrong IP address")
              #  msg.setText("The host could not be resolved")
            except:
                pass

# stabilirea executiei in coada - o instanta pe rand
# se tine cont de durata scanarii

        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()

        q = Queue()
        startTime = time.time()

        for t in range(100):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(self.portmin, self.portmax):
            q.put(worker)

        q.join()
        print('Time taken:', time.time() - startTime, 'seconds')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

