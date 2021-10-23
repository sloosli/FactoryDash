from datetime import datetime
from app.models.kpi_areas import common_dto
from app.services.kpi_areas.db_service import Service as DbService


class Service:
    def __init__(self):
        self.db_service = DbService()

    def get_workshops_json(self, kpi_area_id):
        kpi_values = self.db_service.get_kpi_values_for(kpi_area_id)
        return common_dto.KpiValue.get_list_json(kpi_values)
