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
    def __init__(self, day: datetime, machine_name: str,
                 occupied_percentage: float):
        self.day = day
        self.machine_name = machine_name
        self.occupied_percentage = occupied_percentage
