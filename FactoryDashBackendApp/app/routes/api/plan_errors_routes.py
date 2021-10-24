from flask import Blueprint
#from app.services.kpi_areas.api_service import Service

api_bp = Blueprint('plan_errors', __name__)
#service = Service()


@api_bp.route('/plan_errors/', methods=['GET'])
def get_workshops(kpi_zone: int):
    pass
    #return service.get_workshops_json(kpi_zone)
