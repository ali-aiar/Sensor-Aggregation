import os
from PyQt6.QtWidgets import QApplication

from controllers.sensor_controller import SensorDataController
from views.sensor_view import SensorView

file_path = (os.path.dirname(__file__)) + \
    '/data/sensor_data.json'

sensor_controller = SensorDataController(file_path)
group_data = sensor_controller.get_aggregated_data()


app = QApplication([])


sensor_view = SensorView(group_data)
sensor_view.show()
app.exec()
