from datetime import datetime

from flask import session, render_template

from app.edu.database.crud.CRUDFeedback import CRUDFeedback


class FeedbackController:

    def save_feedback(self, request):
        feedback={
            'feedback': request.form.get('feedback'),
            'user_id': session['logger'],
            'created_on': str(datetime.now()),
            'updated_on': str(datetime.now())
        }

        crudfeedback = CRUDFeedback()
        addfeedback = crudfeedback.add(feedback)

        return render_template("feedback/feedback.html", msg="We have recived your feedback...Thank you")