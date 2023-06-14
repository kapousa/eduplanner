# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sqlalchemy import Column, Integer, String

from app import db
from app.edu.database.models.ModelLessonDesignSection import ModelLessonDesignSection


class CRUDLessonDesignSection:

    def add(self, modelmodel):
        model_model = ModelLessonDesignSection(**modelmodel)
        db.session.commit()
        # Add new profile
        db.session.add(model_model)
        db.session.commit()

        return "success"

    def bulk_add(self, sections):
        db.session.bulk_insert_mappings(ModelLessonDesignSection, sections)
        db.session.commit()
        db.session.close()

        return "success"

    def delete(self, id):
        ModelLessonDesignSection.query.filter_by(id=id).delete()

        return "success"

    def retrieve(self, lesson_design_id):
        modellessondesign = ModelLessonDesignSection.query.filter_by(lesson_design_id=lesson_design_id).all()

        return modellessondesign

