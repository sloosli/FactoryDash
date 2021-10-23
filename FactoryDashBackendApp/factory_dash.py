import sys
from app import create_app
from app.models.machines import db_dto, front_dto
from app.services.machines.db_service import Service as DbService
from app.services.machines.api_service import Service as ApiService

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db_dto': db_dto, 'front_dto': front_dto,
            'DbService': DbService, 'ApiService': ApiService}


is_debug = sys.argv[1] if len(sys.argv) > 1 else False
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=bool(is_debug))
