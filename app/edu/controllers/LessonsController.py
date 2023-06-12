from flask import render_template

from app.edu.libs.Generator import Generator


class LessonsController:

    def generate_lesson(self, request):
        desc= request.form.get("desc")

        generator = Generator()

        lesson_design = generator.generate_lesson_design(desc)

        return render_template("index.html", lesson_design=lesson_design, desc=desc)
