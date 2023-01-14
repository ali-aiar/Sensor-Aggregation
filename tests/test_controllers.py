import unittest
import os
from controllers.sensor_controller import SensorDataController


class TestSensorController(unittest.TestCase):
    def setUp(self):
        file_path = (os.path.dirname(os.path.dirname(__file__))) + \
            '/data/sensor_data.json'
        self.sensor_controller = SensorDataController(file_path)

    def test_aggregate_by_room_and_day(self):
        grouped_data = self.sensor_controller.get_aggregated_data()
        self.assertEqual(
            grouped_data['roomArea1_2020-07-02']['room'], 'roomArea1')
        self.assertEqual(
            grouped_data['roomArea1_2020-07-02']['day'], '2020-07-02')
        self.assertIsNotNone(grouped_data)

