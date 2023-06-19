from flask import request, render_template, session
from flask_login import login_required

from app.edu.controllers.LessonsController import LessonsController
from app.modules.lessons import blueprint


@blueprint.route('/lessons/startreport', methods=['POST', 'GET'])
@login_required
def startreport():
    return render_template("lessons/index.html")

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

@blueprint.route('/lessons/view', methods=['POST', 'GET'])
@login_required
def viewreport():
    lessons_controller = LessonsController()
    report_id = request.args.get('r')
    return lessons_controller.get_report(report_id)

@blueprint.route('/lessons/viewgeneratedreport', methods=['POST', 'GET'])
@login_required
def viewgeneratedreport():
    lessons_controller = LessonsController()
    report_id = session['report_id']
    session.pop('report_id')
    return lessons_controller.get_report(report_id)

@blueprint.route('/lessons/progress', methods=['POST', 'GET'])
@login_required
def progress():
    desc = request.form.get("desc")
    sections = request.form.getlist('sections')
    sections_str = comma_separated_string = ", ".join(sections)
    reportname = request.form.get('reportname')
    return render_template("lessons/progress.html", desc= desc, sections = sections_str, reportname = reportname)



