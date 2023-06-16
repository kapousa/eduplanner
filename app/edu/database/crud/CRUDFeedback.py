# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from app import db
from app.edu.database.models.ModelFeedback import ModelFeedback


class CRUDFeedback:

    def add(self, modelmodel):
        model_model = ModelFeedback(**modelmodel)
        db.session.commit()
        # Add new profile
        db.session.add(model_model)
        db.session.commit()

        return "success"

    def delete(self, id):
        ModelFeedback.query.filter_by(id=id).delete()

        return "success"

    def retrieve_all(self):
        modellessondesign = ModelFeedback.query.order_by('created_on').all()

        return modellessondesign

    def retrieve(self, user_id):
        modellessondesign = ModelFeedback.query.filter_by(user_id=user_id).all()

        return modellessondesign

