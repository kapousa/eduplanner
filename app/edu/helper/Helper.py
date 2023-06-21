from app.edu.constants.Constants import DATABASE, DATABASE_FILE


class Helper:

    @staticmethod
    def downlaod_database():
        path = "{}".format(DATABASE_FILE)
        return path