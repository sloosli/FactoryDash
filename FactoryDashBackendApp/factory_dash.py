import sys
from app import create_app
from app.models import db_dto, front_dto

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db_dto': db_dto, 'front_dto': front_dto}


is_debug = sys.argv[1] if len(sys.argv) > 1 else False
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=bool(is_debug))
