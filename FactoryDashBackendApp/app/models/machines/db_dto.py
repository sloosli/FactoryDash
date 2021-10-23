from datetime import datetime


class WorkShop:
    def __init__(self, id_: int, name: str, machines=None):
        self.id = id_
        self.name = name
        self.machines = machines


class Machine:
    def __init__(self, id_: int, name: str, workshop_id: int):
        self.id = id_
        self.name = name
        self.workshop_id = workshop_id


class MachineDay:
    def __init__(self, day: datetime, day_index: int, occupied_percentage: float,
                 unavailable_percentage: float, machine: Machine):
        self.day = day
        self.day_index = day_index
        self.occupied_percentage = occupied_percentage
        self.unavailable_percentage = unavailable_percentage
        self.machine_id = machine.id
