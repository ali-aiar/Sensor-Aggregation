import os
from PyQt6.QtWidgets import QMainWindow,  QTableWidgetItem
from PyQt6 import uic, QtCore


class SensorView(QMainWindow):
    def __init__(self, sensor_data):
        super().__init__()
        file_path = ((os.path.dirname(__file__))) + \
            '/sensor_view.ui'
        uic.loadUi(file_path, self)
        self.setWindowTitle('Sensor Data Information')
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(9, 150)
        self.create_table(sensor_data)

    def create_table(self, sensor_data):
        i = 0
        for key in sensor_data:
            item1 = self.cell_style(sensor_data[key]['day'])
            item2 = self.cell_style(sensor_data[key]['room'])
            item3 = self.cell_style(
                "%.3f" % sensor_data[key]['temperature_min'])
            item4 = self.cell_style(
                "%.3f" % sensor_data[key]['temperature_max'])
            item5 = self.cell_style(
                "%.3f" % sensor_data[key]['temperature_median'])
            item6 = self.cell_style(
                "%.3f" % sensor_data[key]['temperature_avg'])
            item7 = self.cell_style(
                "%.3f" % sensor_data[key]['humidity_min'])
            item8 = self.cell_style(
                "%.3f" % sensor_data[key]['humidity_max'])
            item9 = self.cell_style(
                "%.3f" % sensor_data[key]['humidity_median'])
            item10 = self.cell_style(
                "%.3f" % sensor_data[key]['humidity_avg'])

            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, item1)
            self.tableWidget.setItem(i, 1, item2)
            self.tableWidget.setItem(i, 2, item3)
            self.tableWidget.setItem(i, 3, item4)
            self.tableWidget.setItem(i, 4, item5)
            self.tableWidget.setItem(i, 5, item6)
            self.tableWidget.setItem(i, 6, item7)
            self.tableWidget.setItem(i, 7, item8)
            self.tableWidget.setItem(i, 8, item9)
            self.tableWidget.setItem(i, 9, item10)

            i = i+1

    def cell_style(self, data):
        item = QTableWidgetItem()
        item.setText(str(data))
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        return item

