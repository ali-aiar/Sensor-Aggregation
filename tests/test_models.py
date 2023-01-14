import unittest
from models.sensor import SensorData
import os


class TestSensorModel(unittest.TestCase):
    def setUp(self):
        file_path = (os.path.dirname(os.path.dirname(__file__))) + \
            '/data/sensor_data.json'
        self.sensor = SensorData(file_path)

    def test_aggregate_by_room_and_day(self):
        grouped_data = self.sensor.aggregate_by_room_and_day()
        self.assertEqual(
            grouped_data['roomArea1_2020-07-02']['room'], 'roomArea1')
        self.assertEqual(
            grouped_data['roomArea1_2020-07-02']['day'], '2020-07-02')
        self.assertIsNotNone(grouped_data)
