from datetime import datetime
from app.utils import Colors
from flask import json


class KpiValue:
    def __init__(self, value: float, date: datetime, index_name: str,
                 target_value: float, warning_border: float, is_higher: bool):
        self.value = float(value)
        self.date = date
        self.index_name = index_name
        self.target_value = target_value
        self.warning_border = warning_border
        self.is_higher = is_higher

    @staticmethod
    def get_list_json(lst):
        return json.dumps({
            'kpi_indexes': [item.get_json() for item in lst]
        }, ensure_ascii=False)

    def get_json(self):
        return {
            "name": self.index_name,
            "score": self.value,
            "gradingData": self.__get_regions()
        }

    def __get_regions(self):
        min_medium = min(self.target_value, self.warning_border)
        max_medium = max(self.target_value, self.warning_border)
        return [{"color": Colors.BAD if self.is_higher else Colors.GOOD,
                 "lowScore": 0,
                 "highScore": min_medium
                 },
                {"color": Colors.MEDIUM,
                 "lowScore": min_medium,
                 "highScore": max_medium
                 },
                {"color": Colors.GOOD if self.is_higher else Colors.BAD,
                 "lowScore": max_medium,
                 "highScore": 100
                 }]
