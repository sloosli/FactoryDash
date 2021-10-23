from datetime import datetime
from app.models.machines import front_dto
from app.services.machines.db_service import Service as DbService


class Service:
    def __init__(self):
        self.db_service = DbService()

    def get_workshops_json(self):
        db_workshops = self.db_service.get_all_workshops()
        front_workshops = [front_dto.WorkShop(workshop)
                           for workshop in db_workshops]
        return front_dto.WorkShop.get_list_json(front_workshops)

    def get_machines_json(self, workshop_id):
        db_machines = self.db_service.get_machines_in_workshop(workshop_id)
        front_machines = [front_dto.Machine(machine)
                          for machine in db_machines]
        return front_dto.Machine.get_list_json(front_machines)

    def get_workshop_schedule(self, workshop_id: int,
                              start_date: datetime, end_date: datetime):
        db_machine_days = self.db_service.get_days_state_for_workshop(
            workshop_id, start_date, end_date)
        machines_schedule = front_dto.MachinesSchedule(db_machine_days)
        return front_dto.MachinesSchedule.get_list_json(machines_schedule)

    def get_machine_schedule(self, machine_id: int, start_date: datetime,
                             end_date: datetime):
        db_machine_days = self.db_service.get_days_state_for_machine(
            machine_id, start_date, end_date)
        machines_schedule = front_dto.MachinesSchedule(db_machine_days)
        return front_dto.MachinesSchedule.get_list_json(machines_schedule)
