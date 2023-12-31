# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for, session
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from app import db, login_manager
from app.authentication import blueprint
from app.authentication.forms import LoginForm, CreateAccountForm
from app.base.models import User
import datetime
from app.authentication.util import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))


# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    try:
        login_form = LoginForm(request.form)
        if 'login' in request.form:

            # read form data
            username = request.form['username']
            password = request.form['password']

            # Locate user
            user = User.query.filter_by(username=username).first()

            # Check the password
            if user and verify_pass(password, user.password):

                login_user(user)
                session['logged_in'] = True
                session['logger'] = user.id
                return redirect(url_for('lessons_blueprint.startreport'))

            # Something (user or pass) is not ok
            return render_template('accounts/login.html',
                                   msg='Wrong user or password',
                                   form=login_form)

        if not current_user.is_authenticated:
            return render_template('accounts/login.html',
                                   form=login_form)
        return render_template('accounts/login.html',
                                   form=login_form)
    except Exception as e:
        print(e)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    current_time = datetime.datetime.now()
    create_account_form = CreateAccountForm(request.form)

    if 'register' in request.form:

        if not create_account_form.validate(): # Validate inputs
            return render_template('accounts/register.html', form=create_account_form)

        username = request.form['username']
        email = request.form['email']
        pp =request.form['password']
        cpp = request.form['confirm_password']
        at= request.form['account_type']

        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form, current_time=current_time)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form, current_time=current_time)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template('accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=create_account_form, current_time=current_time)

    else:
        return render_template('accounts/register.html', form=create_account_form, current_time=current_time)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))


# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500
