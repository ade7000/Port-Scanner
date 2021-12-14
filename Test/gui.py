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
        self.ip_label.setGeometry(QtCore.QRect(10, 10, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ip_label.setFont(font)
        self.ip_label.setText(_translate("MainWindow", "What are the IP addresses"))

        self.ip_label2 = QtWidgets.QLabel(self.centralwidget)
        self.ip_label2.setGeometry(QtCore.QRect(10, 40, 301, 51))
        self.ip_label2.setFont(font)
        self.ip_label2.setText(_translate("MainWindow", "or the Subnet?"))

        self.input_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ip.setGeometry(QtCore.QRect(10, 90, 241, 141))

        #********************************************************
        #Port Range Form
        #********************************************************

        self.ports_label = QtWidgets.QLabel(self.centralwidget)
        self.ports_label.setGeometry(QtCore.QRect(10, 220, 281, 81))
        self.ports_label.setFont(font)
        self.ports_label.setText(_translate("MainWindow", "What is the range of ports?"))

        self.warning_ports = QtWidgets.QLabel(self.centralwidget)
        self.warning_ports.setGeometry(QtCore.QRect(20, 280, 290, 21))
        font.setPointSize(13)
        self.warning_ports.setFont(font)
        self.warning_ports.setText(_translate("MainWindow", "If no ports specified, scan the first "))
        self.warning2_ports = QtWidgets.QLabel(self.centralwidget)
        self.warning2_ports.setGeometry(QtCore.QRect(20, 290, 101, 41))
        self.warning2_ports.setFont(font)
        self.warning2_ports.setText(_translate("MainWindow", "1024 ports."))

        self.input_ports = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ports.setGeometry(QtCore.QRect(20, 330, 181, 31))

        #*********************************************************
        #Output Box
        #*********************************************************
        
        self.output_scan = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_scan.setGeometry(QtCore.QRect(310,10,481,311))
        font.setPointSize(14)
        self.output_scan.setFont(font)
        
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
        self.input_outfile.setGeometry(QtCore.QRect(340, 390, 250, 31))

        self.outfile_label2 = QtWidgets.QLabel(self.centralwidget)
        self.outfile_label2.setGeometry(QtCore.QRect(340,410,461,50))
        self.outfile_label2.setFont(font)
        self.outfile_label2.setText(_translate("MainWindow", "(You will still see the scanning, but it's saving at the end)"))

        self.outfile_button = QtWidgets.QPushButton(self.centralwidget)
        self.outfile_button.setGeometry(QtCore.QRect(630,390,91,31))
        self.outfile_button.setText(_translate("MainWindow", "Submit"))

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
        
          
        if(self.input_outfile.text()==''):
            pass
        else:
            filename=self.input_outfile.text()
            f = open(filename,"x")
        self.scanning()
        
        
    def scanning(self):
        socket.setdefaulttimeout(1)
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
                    print("Port %s is open. Service name: %s" %(port,socket.getservbyport(port,"tcp")
                    print(con)
                    con.close()
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

