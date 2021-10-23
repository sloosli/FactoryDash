from typing import List
from collections import defaultdict
from flask import json
import app.models.machines.db_dto as db_models


class WorkShop:
    def __init__(self, db_workshop: db_models.WorkShop):
        self.id = db_workshop.id
        self.name = db_workshop.name

    @staticmethod
    def get_list_json(lst):
        return json.dumps({
            'workshops': [item.__dict__ for item in lst]
        }, ensure_ascii=False)


class Machine:
    def __init__(self, machine: db_models.Machine):
        self.id = machine.id
        self.name = machine.name

    @staticmethod
    def get_list_json(lst):
        return json.dumps({
            'machines': [item.__dict__ for item in lst]
        }, ensure_ascii=False)


class MachinesSchedule:
    def __init__(self, machine_days: List[db_models.MachineDay]):
        self.machine_states = defaultdict(list)
        for state in machine_days:
            self.machine_states[state.machine_name].append(
                state.occupied_percentage)
        self.days = sorted(set(map(lambda m_day: m_day.day, machine_days)))

    @staticmethod
    def get_list_json(schedule):
        return json.dumps({
            'states': [{
                'machine': machine_name,
                'occupied': schedule.machine_states[machine_name]
            } for machine_name in schedule.machine_states],
            'days': [day.strftime("%d.%m.%Y") for day in schedule.days]
        }, ensure_ascii=False)
