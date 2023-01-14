from models.sensor import SensorData


class SensorDataController:
    def __init__(self, filepath: str):
        self.model = SensorData(filepath)

    def get_aggregated_data(self):
        return self.model.aggregate_by_room_and_day()
