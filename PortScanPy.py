# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
import socket
import time
import threading
import os
import ipaddress

from queue import Queue

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        #setting the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(550,300,800, 470)
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

        self.input_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.input_ip.setGeometry(QtCore.QRect(10, 90, 241, 121))

        #Checkbox
        self.checkhost = QtWidgets.QCheckBox(self.centralwidget)
        self.checkhost.setGeometry(QtCore.QRect(10, 220, 241, 25))
        font.setPointSize(13)
        self.checkhost.setFont(font)
        self.checkhost.setText(_translate("MainWindow", "Don\'t show the hosts down"))

        #********************************************************
        #Port Range Form
        #********************************************************

        self.ports_label = QtWidgets.QLabel(self.centralwidget)
        self.ports_label.setGeometry(QtCore.QRect(10, 245, 281, 31))
        font.setPointSize(17)
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
        self.outfile_label2.setText(_translate("MainWindow", "(This will save everything that is on the output box)"))
        #Submit button for output file
        self.outfile_button = QtWidgets.QPushButton(self.centralwidget)
        self.outfile_button.setGeometry(QtCore.QRect(630,390,91,31))
        self.outfile_button.setText(_translate("MainWindow", "Submit"))
        
        self.outfile_button.clicked.connect(self.outputfile)

        #***********************************************************
        #Buttons
        #***********************************************************

        #Start
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(145, 370, 121, 76))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.start_button.clicked.connect(self.verifying)

        #Clear
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(25, 370, 121, 76))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.clear_button.clicked.connect(self.clearing)


        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def clearing(self):
        self.output_scan.clear()

    def verifying(self): 
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
        
        #Verifying the IP address
        IPs=self.input_ip.toPlainText().splitlines()
        for i in range(len(IPs)):
            if(IPs[i]==''):
                pass
            else:
                ip=str(IPs[i])
                if ("/" in ip):
                    subnet=ipaddress.ip_network(ip)
                    nr = 0
                    for x in subnet.hosts():
                        HOST_UP= True if os.system("ping -t2 -c 1 " + str(x)) is 0 else False
                        if (HOST_UP==1):
                            self.scanning(str(x))
                            nr +=1
                        elif (self.checkhost.isChecked()==1):
                            pass
                        else:
                            self.output_scan.append("Host {} is down".format(str(x)))
                            self.output_scan.append('\n')

                    if (nr == 0):
                        self.output_scan.append("No host alive on {} subnet".format(str(ip)))
                else:
                    HOST_UP= True if os.system("ping -t3 -c 1 " + ip) is 0 else False
                    if (HOST_UP==1):
                        self.scanning(ip)
                        
                    elif (self.checkhost.isChecked()==1):
                        pass
                    else:
                        self.output_scan.append("Host {} is down".format(str(ip)))
                        self.output_scan.append('\n')
      

    def outputfile(self):
        if(self.input_outfile.text()==''):
            pass
        else:
            filename=self.input_outfile.text()
            with open(filename+".txt", "a") as f:
                f.write(self.output_scan.toPlainText())
            
        
        
    def scanning(self,ip):
        socket.setdefaulttimeout(1)
        print_lock = threading.Lock()
        
        #try:
        t_IP = socket.gethostbyname(ip)
        print1="Starting scan on host: "+t_IP
        self.output_scan.append(print1);

        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))
                with print_lock:
                    self.output_scan.append("Port %s is open. Service name: %s" %(port,socket.getservbyport(port,"tcp")))
			
                    con.close()
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

        for t in range(10):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(self.portmin, self.portmax):
            q.put(worker)

        q.join()
        print2="Time taken: "+ str(time.time() - startTime)+ " seconds"
        self.output_scan.append(print2)
        self.output_scan.append('\n')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
