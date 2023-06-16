from flask import request, render_template
from flask_login import login_required

from app.edu.controllers.FeedbackController import FeedbackController
from app.modules.feedback import blueprint


@blueprint.route('/feedback/sendfeedback', methods=['POST', 'GET'])
@login_required
def sendfeedback():
    return render_template("feedback/feedback.html", msg='')

@blueprint.route('/feedback/add', methods=['POST', 'GET'])
@login_required
def add():
    feedbackcontroller = FeedbackController()
    return feedbackcontroller.save_feedback(request)




