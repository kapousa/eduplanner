# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from app import db
from app.edu.database.models.ModelLessonDesign import ModelLessonDesign


class CRUDLessonDesign:

    def add(self, modelmodel):
        model_model = ModelLessonDesign(**modelmodel)
        db.session.commit()
        # Add new profile
        db.session.add(model_model)
        db.session.commit()

        return "success"

    def delete(self, id):
        ModelLessonDesign.query.filter_by(id=id).delete()

        return "success"

    def retrieve_all(self, user_id):
        modellessondesign = ModelLessonDesign.query.filter_by(user_id=user_id).order_by('lesson_design_name').all()

        return modellessondesign

    def retrieve(self, report_id):
        modellessondesign = ModelLessonDesign.query.with_entities(ModelLessonDesign.id, ModelLessonDesign.desc, ModelLessonDesign.lesson_design_name).filter_by(id=report_id).first()

        return modellessondesign

