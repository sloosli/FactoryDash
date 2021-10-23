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
        self.day = machine_day.day.strftime("%Y%m%d")


class MachinesSchedule:
    def __init__(self, machine_days: List[db_models.MachineDay]):
        self.machines = [MachinesSchedule.make_group_dict(machine_id, group)
                         for machine_id, group in groupby(
                machine_days, lambda x: x.machine_id)]

    @staticmethod
    def make_group_dict(machine_id, group):
        group_list = [MachineStatus(machine_day).__dict__
                      for machine_day in group]
        return {
            "machine_id": machine_id,
            "statuses": group_list
        }

    @classmethod
    def get_list_json(cls, schedule):
        return json.dumps({
            "schedule": schedule.machines
        })
