import json
from datetime import datetime
from statistics import mean, median


class SensorData:
    def __init__(self, filepath: str):
        with open(filepath, 'r') as f:
            self.data = json.load(f)

    def aggregate_by_room_and_day(self):
        # Group sensor data by room and day
        grouped_data = {}
        for sensor in self.data['array']:
            room = sensor['roomArea']
            day = datetime.fromtimestamp(
                sensor['timestamp'] / 1e3).strftime('%Y-%m-%d')
            key = f"{room}_{day}"
            if key not in grouped_data:
                grouped_data[key] = {
                    'room': room,
                    'day': day,
                    'temperature': [],
                    'humidity': []
                }
            grouped_data[key]['temperature'].append(sensor['temperature'])
            grouped_data[key]['humidity'].append(sensor['humidity'])

        # Calculate min, max, median, and avg for temperature and humidity
        for key in grouped_data:
            grouped_data[key]['temperature_min'] = min(
                grouped_data[key]['temperature'])
            grouped_data[key]['temperature_max'] = max(
                grouped_data[key]['temperature'])
            grouped_data[key]['temperature_median'] = median(
                grouped_data[key]['temperature'])
            grouped_data[key]['temperature_avg'] = mean(
                grouped_data[key]['temperature'])
            grouped_data[key]['humidity_min'] = min(
                grouped_data[key]['humidity'])
            grouped_data[key]['humidity_max'] = max(
                grouped_data[key]['humidity'])
            grouped_data[key]['humidity_median'] = median(
                grouped_data[key]['humidity'])
            grouped_data[key]['humidity_avg'] = mean(
                grouped_data[key]['humidity'])

        return grouped_data
