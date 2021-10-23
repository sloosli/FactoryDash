from flask import Blueprint
from app.services.kpi_areas.api_service import Service

api_bp = Blueprint('kpi_api', __name__)
service = Service()


@api_bp.route('/kpi_index_value/<int:kpi_zone>', methods=['GET'])
def get_workshops(kpi_zone: int):
    return service.get_workshops_json(kpi_zone)
