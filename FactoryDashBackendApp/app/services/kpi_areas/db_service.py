from app.models.kpi_areas.common_dto import *
from app.services.common.db_service import BaseDbService


class Service(BaseDbService):
    def __init__(self):
        super(Service, self).__init__()

    def get_kpi_values_for(self, kpi_area_id: int):
        kpi_area_id = int(kpi_area_id)
        request = "select kf.val_percent, kf.dt_metric, ki.index_name, " \
                  "kl.target_val, kl.warning_val, kl.if_more\n" \
                  "from kpe_fact kf, kpe_indexes ki,\n kpi_limits kl\n" \
                  f"where kf.area_id = {kpi_area_id}\n" \
                  "and kf.index_id = ki.index_id\n" \
                  "and kf.dt_metric = (select max(dt_metric) from kpe_fact)" \
                  "and kf.index_id = kl.index_id;"
        raw_kpi_values = self._execute_request(request)
        return Service._make_list_of(KpiValue, raw_kpi_values)
