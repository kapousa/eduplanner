from flask import request
from flask_login import login_required

from app.edu.controllers.LessonsController import LessonsController
from app.modules.lessons import blueprint




@blueprint.route('/lessons/generatelesson', methods=['POST'])
@login_required
def generatelesson():
    lessons_controller = LessonsController()

    return lessons_controller.generate_lesson(request)



