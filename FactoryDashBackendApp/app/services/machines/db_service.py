from typing import List, Tuple
import psycopg2
from app.models.machines.db_dto import *


class Service:
    def __init__(self):
        # TODO: вынести в конфигу, пока некритично, т.к. недоступна извне
        self.connection = psycopg2.connect(dbname='accenture', user='postgres',
                                           password='pdp565',
                                           host='192.168.50.128')

    def get_all_workshops(self):
        raw_workshops = self.__execute_request("select * from shops;")
        return Service.__make_list_of(WorkShop, raw_workshops)

    def get_machines_in_workshop(self, workshop_id: int):
        workshop_id = int(workshop_id)
        request = "select a.agregate_id, a.agregate_name, a.shop_id\n" + \
                  "from aggregates a, shops s\n" + \
                  "where a.shop_id = s.shop_id\n" + \
                  f"and a.shop_id = {workshop_id};"
        raw_machines = self.__execute_request(request)
        return Service.__make_list_of(Machine, raw_machines)

    def get_days_state_for_workshop(self, workshop_id: int,
                                    start_date: datetime, end_date: datetime):
        request = "TODO"
        raw_machines_days = self.__execute_request(request)
        return Service.__make_list_of(MachineDay, raw_machines_days)

    def get_days_state_for_machine(self, machine_id: int,
                                   start_date: datetime, end_date: datetime):
        request = "TODO"
        raw_machines_days = self.__execute_request(request)
        return Service.__make_list_of(MachineDay, raw_machines_days)

    def __execute_request(self, request: str):
        with self.connection.cursor() as cursor:
            cursor.execute(request)
            return cursor.fetchall()

    @staticmethod
    def __make_list_of(type_: type, raw_data: List[Tuple[int, str]]):
        return list(map(lambda raw: type_(*raw), raw_data))
