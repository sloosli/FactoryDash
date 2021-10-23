from typing import List, Tuple
import psycopg2


class BaseDbService:
    def __init__(self):
        self.connection = BaseDbService.connect()

    @staticmethod
    def connect():
        # TODO: вынести в конфигу, пока некритично, т.к. недоступна извне
        return psycopg2.connect(dbname='accenture', user='postgres',
                                password='pdp565',
                                host='192.168.50.128')

    @staticmethod
    def _make_list_of(type_: type, raw_data: List[Tuple[int, str]]):
        return list(map(lambda raw: type_(*raw), raw_data))

    def _execute_request(self, request: str, raise_error: bool = False):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(request)
                return cursor.fetchall()
        except psycopg2.InterfaceError:
            if raise_error:
                raise
            self.connection = self.connection = BaseDbService.connect()
            return self._execute_request(request, True)
