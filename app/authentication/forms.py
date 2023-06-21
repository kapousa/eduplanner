# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, EqualTo, Regexp, Length


# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                           id='username_login',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    first_name = StringField('First Name',
                             id='first_name',
                             validators=[DataRequired()])
    last_name = StringField('Last Name',
                            id='last_name',
                            validators=[DataRequired()])
    username = StringField('Username',
                           id='username_create',
                           validators=[DataRequired(), Regexp(r'^[A-Za-z0-9]+$', message='Username must contain only letters and numbers')])
    email = StringField('Email',
                        id='email_create',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='password',
                             validators=[DataRequired(),
                                         Length(min=6, message='Minium length of password is 6'),
                                         Regexp(
                                             r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$',
                                             message='Password must have at least one capital letter, one special character, and one number'
                                         )])
    confirm_password = PasswordField('Confirm Password',
                                     id='confirm_password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
