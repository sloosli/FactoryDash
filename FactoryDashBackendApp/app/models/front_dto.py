from itertools import groupby
from typing import List
from flask import json
import app.models.db_dto as db_models


class WorkShop:
    def __init__(self, db_workshop: db_models.WorkShop):
        self.id = db_workshop.id
        self.name = db_workshop.name

    @classmethod
    def get_list_json(cls, lst):
        return json.dumps({
            'workshops': [item.__dict__ for item in lst]
        }, ensure_ascii=False)


class Machine:
    def __init__(self, machine: db_models.Machine):
        self.id = machine.id
        self.name = machine.name

    @classmethod
    def get_list_json(cls, lst):
        return json.dumps({
            'machines': [item.__dict__ for item in lst]
        }, ensure_ascii=False)


class MachineStatus:
    def __init__(self, machine_day: db_models.MachineDay):
        self.occupied_percentage = machine_day.occupied_percentage
        self.unavailable_percentage = machine_day.unavailable_percentage
        self.machine_id = machine_day.machine_id


class MachineSchedule:
    def __init__(self, machine_days: List[db_models.MachineDay]):
        self.days = {key.strftime("%Y%m%d"): [MachineStatus(value) for value in group]
                     for key, group in groupby(machine_days, lambda x: x.day)}

    @classmethod
    def get_list_json(cls, schedule):
        return json.dumps({
            "schedule": [
                {
                    "date": date,
                    "machine_statuses": [status.__dict__ for status in schedule.days[date]]
                } for date in schedule.days
            ]
        })
