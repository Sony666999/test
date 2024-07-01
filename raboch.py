from PyQt5 import Qt
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget,QTableWidgetItem
import sys
from library import*

app = QtWidgets.QApplication([])
win = uic.loadUi("rabochue.ui")

data = EmployeeData()
data.read_data_from_file("text.txt")

def btn_load_table():
    win.tableWidget.setRowCount(len(data.employees))
    row = 0
    for employee in data.employees.values():
        win.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(employee.fio))
        win.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(employee.department))
        win.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(employee.work_days)))
        win.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(employee.salary)))
        row += 1

def btn_append_person():
    fio = " ".join(win.lineEdit4.text().split())
    department = win.lineEdit5.text()
    work_days = int(win.lineEdit6.text())
    salary = int(win.lineEdit7.text())
    data.employees[fio] = Employee(fio, department, work_days, salary)
    data.save_data_to_file("text.txt")
    btn_load_table()

def btn_edit_person():
    row = win.tableWidget.currentRow()
    if row != -1:
        fio = " ".join(win.tableWidget.item(row, 0).text().split())
        department = win.tableWidget.item(row, 1).text()
        work_days = int(win.tableWidget.item(row, 2).text())
        salary = int(win.tableWidget.item(row, 3).text())
        data.employees[fio] = Employee(fio, department, work_days, salary)
        data.save_data_to_file("text.txt")
        btn_load_table()

def btn_del_person():
    row = win.tableWidget.currentRow()
    if row != -1:
        fio = " ".join(win.tableWidget.item(row, 0).text().split())
        data.employees.pop(fio, None)
        data.save_data_to_file("text.txt")
        btn_load_table()

win.pushButton.clicked.connect(btn_load_table)
win.pushButton_3.clicked.connect(btn_append_person)
win.pushButton_4.clicked.connect(btn_edit_person)
win.pushButton_5.clicked.connect(btn_del_person)

win.show()
sys.exit(app.exec_())
