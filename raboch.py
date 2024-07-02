from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget,QTableWidgetItem
import sys
from library import*

app = QtWidgets.QApplication([])
win = uic.loadUi("рабочие.ui")

Gr = Grup()
Gr.read_data_from_file("text.txt")
print("Количество: ", Gr.count)


def btnLoadTable():

    win.tableWidget.setRowCount(Gr.count) 
    row = 0
    for x in Gr.A:
        print(1)
       
        win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].fam+' '+Gr.A[x].name+' '+Gr.A[x].otchestvo))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].number))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].days))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(Gr.A[x].moneys))
        row += 1

def btnAppendPerson():
    
    strPerson = win.lineEdit.text()
   
    Gr.appendPerson(strPerson)
  
    win.tableWidget.clear()
    btnLoadTable()
   
 
  
win.pushButton.clicked.connect(btnLoadTable)
print(Gr.A[0].getPerson_forTable())

win.pushButton_3.clicked.connect(btnAppendPerson)

win.show()
sys.exit(app.exec())
