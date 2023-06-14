from flask import request, render_template
from flask_login import login_required

from app.edu.controllers.LessonsController import LessonsController
from app.modules.lessons import blueprint


@blueprint.route('/lessons/startreport', methods=['POST', 'GET'])
@login_required
def startreport():
    return render_template("application/pages/lessons/index.html")

@blueprint.route('/lessons/generatelesson', methods=['POST', 'GET'])
@login_required
def generatelesson():
    lessons_controller = LessonsController()
    return lessons_controller.generate_lesson(request)

@blueprint.route('/lessons/myreports', methods=['POST', 'GET'])
@login_required
def myreports():
    lessons_controller = LessonsController()
    return lessons_controller.get_all_reports()

@blueprint.route('/lessons/<report_id>/view', methods=['POST', 'GET'])
@login_required
def viewreport(report_id):
    lessons_controller = LessonsController()
    return lessons_controller.get_report(report_id)



