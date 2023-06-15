import traceback

from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from app import login_manager
from app.base import blueprint


@blueprint.route('/index')
@login_required
def index():
    return render_template('lessons/index.html', segment='index')

@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/base/FILE.html
        return render_template("base/" + template, segment=segment)

    except TemplateNotFound:
        #return render_template('base/page-404.html'), 404
        return render_template('page-404.html'), 404
    except:
        # return render_template('base/page-500.html'), 500
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None



## Errors
@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('page-403.html', error="Access Forbidden - Please authenticate using Login page", segment='error'), 403

@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html', error="Access Forbidden - Please authenticate using Login page", segment='error'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html', error="Page Not Found", segment='error'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    tb = traceback.format_exc()
    return render_template(('page-500.html'), error=error, traceback=tb, segment='error'), 500
