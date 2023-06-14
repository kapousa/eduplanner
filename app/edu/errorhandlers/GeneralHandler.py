from flask import render_template


class GeneralHandler:

    def general_error(self, error_code, error):
        return render_template('page-{}.html'.format(error_code), error=error)
