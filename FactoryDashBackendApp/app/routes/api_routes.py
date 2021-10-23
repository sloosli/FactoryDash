from datetime import datetime
from flask import Blueprint, abort, request
from app.services.api_service import Service
from app.utils import get_datetime_or_today

api_bp = Blueprint('api', __name__)
service = Service(True)


@api_bp.route('/workshops', methods=['GET'])
def get_workshops():
    return service.get_workshops_json()


@api_bp.route('/machines/<int:workshop_id>', methods=['GET'])
def get_machines(workshop_id: int):
    if workshop_id < 1:
        abort(404)
    return service.get_machines_json(workshop_id)


@api_bp.route('/machine_schedule', methods=['GET'])
def get_machine_schedule():
    workshop_id = request.args.get('workshop_id', default=-1, type=int)
    machine_id = request.args.get('machine_id', default=-1, type=int)
    if workshop_id < 1 and machine_id < 1:
        return abort(400)

    start_date = get_datetime_or_today(request.args, 'start_date')
    end_date = get_datetime_or_today(request.args, 'end_date')

    if workshop_id > 0:
        return service.get_workshop_schedule(workshop_id, start_date, end_date)
    return service.get_machine_schedule(machine_id, start_date, end_date)
