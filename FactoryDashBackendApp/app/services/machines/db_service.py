from app.models.machines.db_dto import *
from app.services.common.db_service import BaseDbService


class Service(BaseDbService):
    def __init__(self):
        super(Service, self).__init__()

    def get_all_workshops(self):
        raw_workshops = self._execute_request("select * from shops;")
        return Service._make_list_of(WorkShop, raw_workshops)

    def get_machines_in_workshop(self, workshop_id: int):
        workshop_id = int(workshop_id)

        request = "select res_id, res_name, shop_id\n" + \
                  "from resources r \n" + \
                  f"where shop_id = {workshop_id};"
        raw_machines = self._execute_request(request)
        return Service._make_list_of(Machine, raw_machines)

    def get_days_state_for_workshop(self, workshop_id: int,
                                    start_date: datetime, end_date: datetime):
        workshop_id = int(workshop_id)
        if type(start_date) != datetime or type(end_date) != datetime:
            raise ValueError()
        start_date_str = start_date.strftime("%d.%m.%Y")
        end_date_str = end_date.strftime("%d.%m.%Y")
        request = "select ald.plan_for_day, res.res_name, " + \
                  "ald.occupied_percentage occ\n" + \
                  "from aggregates_loadup_det ald, resources res\n" + \
                  f"where ald.shop_id = {workshop_id}\n" + \
                  "and ald.res_id = res.res_id\n" + \
                  "and ald.dt_plan = date ('07.10.2021')" \
                  f"and plan_for_day >= date ('{start_date_str}')" \
                  f"and plan_for_day <= date ('{end_date_str}') \n" + \
                  "and duration_in_days = 1\n" + \
                  "order by plan_for_day;"
        raw_machines_days = self._execute_request(request)
        return Service._make_list_of(MachineDay, raw_machines_days)

    def get_days_state_for_machine(self, machine_id: int,
                                   start_date: datetime, end_date: datetime):
        machine_id = int(machine_id)
        if type(start_date) != datetime or type(end_date) != datetime:
            raise ValueError()
        start_date_str = start_date.strftime("%d.%m.%Y")
        end_date_str = end_date.strftime("%d.%m.%Y")
        request = "select ald.plan_for_day, res.res_name, " + \
                  "ald.occupied_percentage occ\n" + \
                  "from aggregates_loadup_det ald, resources res\n" + \
                  f"where ald.res_id = {machine_id}\n" \
                  "and ald.res_id = res.res_id\n" + \
                  "and ald.dt_plan = date ('07.10.2021')" \
                  f"and ald.plan_for_day >= date ('{start_date_str}')" \
                  f"and ald.plan_for_day <= date ('{end_date_str}') \n" + \
                  "and ald.duration_in_days = 1\n" + \
                  "order by ald.plan_for_day;"
        raw_machines_days = self._execute_request(request)
        return Service._make_list_of(MachineDay, raw_machines_days)
