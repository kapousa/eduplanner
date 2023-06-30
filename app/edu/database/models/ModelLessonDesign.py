# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sqlalchemy import Column, Integer, String

from app import db


class ModelLessonDesign(db.Model):

    __tablename__ = 'lesson_design'

    id = Column(String, primary_key=True, unique=True)
    lesson_design_name = Column(String)
    desc = Column(String)
    user_id = Column(Integer)
    created_on = Column(String)
    updated_on = Column(String)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)
        setattr(self, property, value)

    def __repr__(self):
        return str(self.model_id)



