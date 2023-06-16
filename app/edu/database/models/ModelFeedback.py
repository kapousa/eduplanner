# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sqlalchemy import Column, Integer, String

from app import db


class ModelFeedback(db.Model):

    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    feedback = Column(String)
    user_id = Column(String)
    created_on = Column(String)
    updated_on = Column(String)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)
        setattr(self, property, value)

    def __repr__(self):
        return str(self.model_id)



