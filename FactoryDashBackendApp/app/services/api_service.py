from app.models import db_dto, front_dto
from datetime import datetime


class Service:
    workshops = [
        db_dto.WorkShop(1, 'Конвертерный цех 1 УНРС 2,3,4,6'),
        db_dto.WorkShop(2, 'Конвертеры КЦ-1'),
        db_dto.WorkShop(3, 'Конвертерный цех 2 УНРС 5,6,7,8,9'),
    ]
    machines = [
        db_dto.Machine(1, 'УНРС-2', workshops[0]),
        db_dto.Machine(2, 'УНРС-3', workshops[0]),
        db_dto.Machine(3, 'УНРС-4', workshops[0]),
        db_dto.Machine(4, 'УНРС-6', workshops[0]),

        db_dto.Machine(5, 'К-1', workshops[1]),
        db_dto.Machine(6, 'К-2', workshops[1]),
        db_dto.Machine(7, 'К-3', workshops[1]),
        db_dto.Machine(8, 'УНРС-5', workshops[2]),
        db_dto.Machine(9, 'УНРС-6', workshops[2]),
        db_dto.Machine(10, 'УНРС-7', workshops[2]),
        db_dto.Machine(11, 'УНРС-8', workshops[2]),
        db_dto.Machine(12, 'УНРС-9', workshops[2]),
    ]
    machine_days = [
        db_dto.MachineDay(datetime(2021, 10, 7), 0, 100, 65.4, machines[0]),
        db_dto.MachineDay(datetime(2021, 10, 7), 0, 29, 73.5, machines[1]),
        db_dto.MachineDay(datetime(2021, 10, 7), 0, 100, 74.1, machines[2]),
        db_dto.MachineDay(datetime(2021, 10, 7), 0, 100, 67.4, machines[3]),

        db_dto.MachineDay(datetime(2021, 10, 7), 0, 42, 44.1, machines[4]),
        db_dto.MachineDay(datetime(2021, 10, 7), 0, 100, 41.1, machines[5]),
        db_dto.MachineDay(datetime(2021, 10, 7), 0, 8, 16.9, machines[6]),

        db_dto.MachineDay(datetime(2021, 10, 8), 1, 100, 32.3, machines[0]),
        db_dto.MachineDay(datetime(2021, 10, 8), 1, 50, 36.5, machines[1]),
        db_dto.MachineDay(datetime(2021, 10, 8), 1, 100, 86.6, machines[2]),
        db_dto.MachineDay(datetime(2021, 10, 8), 1, 58, 89.1, machines[3]),

        db_dto.MachineDay(datetime(2021, 10, 8), 1, 100, 15.25, machines[4]),
        db_dto.MachineDay(datetime(2021, 10, 8), 1, 63, 54.45, machines[5]),
        db_dto.MachineDay(datetime(2021, 10, 8), 1, 100, 84.147, machines[6]),

        db_dto.MachineDay(datetime(2021, 10, 9), 2, 100, 25.25, machines[0]),
        db_dto.MachineDay(datetime(2021, 10, 9), 2, 79, 12.43, machines[1]),
        db_dto.MachineDay(datetime(2021, 10, 9), 2, 100, 252.5, machines[2]),
        db_dto.MachineDay(datetime(2021, 10, 9), 2, 61, 95.57458, machines[3]),

        db_dto.MachineDay(datetime(2021, 10, 9), 2, 100, 43.12, machines[4]),
        db_dto.MachineDay(datetime(2021, 10, 9), 2, 75, 4523., machines[5]),
        db_dto.MachineDay(datetime(2021, 10, 9), 2, 100, 30.429, machines[6]),

        db_dto.MachineDay(datetime(2021, 10, 10), 3, 50, 54.6, machines[0]),
        db_dto.MachineDay(datetime(2021, 10, 10), 3, 100, 59.98, machines[1]),
        db_dto.MachineDay(datetime(2021, 10, 10), 3, 100, 94.547, machines[2]),
        db_dto.MachineDay(datetime(2021, 10, 10), 3, 72, 97.3, machines[3]),

        db_dto.MachineDay(datetime(2021, 10, 10), 3, 86, 72.3423, machines[4]),
        db_dto.MachineDay(datetime(2021, 10, 10), 3, 100, 74.237, machines[5]),
        db_dto.MachineDay(datetime(2021, 10, 10), 3, 100, 78.62, machines[6]),
    ]

    def __init__(self, is_debug: bool = True):
        self.is_debug = is_debug
        if is_debug:
            self.workshops = Service.workshops.copy()
            self.machines = Service.machines.copy()
            self.machine_days = Service.machine_days.copy()

    @staticmethod
    def __get_machine_id_checker(machine_id):
        def __is_machine_id_valid(machine_day):
            return machine_day.machine_id == machine_id

        return __is_machine_id_valid

    @staticmethod
    def __get_machine_date_valid_checker(start_date: datetime,
                                         end_date: datetime,
                                         *addition_checkers):
        def __is_machine_day_valid(machine_day: db_dto.MachineDay):
            for checker in addition_checkers:
                if not checker(machine_day):
                    return False
            return start_date.day <= machine_day.day.day <= end_date.day

        return __is_machine_day_valid

    @staticmethod
    def __convert_machine_days_to_json(machine_days, valid_checker):
        filtered_machine_days = list(filter(valid_checker, machine_days))
        machine_schedule = front_dto.MachineSchedule(filtered_machine_days)
        return front_dto.MachineSchedule.get_list_json(machine_schedule)

    def get_workshops_json(self):
        front_workshops = [front_dto.WorkShop(workshop)
                           for workshop in self.workshops]
        return front_dto.WorkShop.get_list_json(front_workshops)

    def get_machines_json(self, workshop_id):
        machines_in_workshop = filter(
            lambda machine: machine.workshop_id == workshop_id,
            self.machines)
        front_machines = [front_dto.Machine(machine)
                          for machine in machines_in_workshop]
        return front_dto.Machine.get_list_json(front_machines)

    def get_workshop_schedule(self, workshop_id: int, start_date: datetime,
                              end_date: datetime):
        machines = list(map(lambda machine: machine.id,
                            filter(lambda machine:
                                   machine.workshop_id == workshop_id,
                                   self.machines)))
        valid_checker = Service.__get_machine_date_valid_checker(
            start_date, end_date, lambda machine_day:
            machine_day.machine_id in machines)
        return Service.__convert_machine_days_to_json(self.machine_days,
                                                      valid_checker)

    def get_machine_schedule(self, machine_id: int, start_date: datetime,
                             end_date: datetime):
        id_checker = Service.__get_machine_id_checker(machine_id)
        valid_checker = Service.__get_machine_date_valid_checker(
            start_date, end_date, id_checker)
        return Service.__convert_machine_days_to_json(self.machine_days,
                                                      valid_checker)
