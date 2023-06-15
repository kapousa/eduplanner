from flask import render_template, session

from app.edu.database.crud.CRUDLessonDesign import CRUDLessonDesign
from app.edu.database.crud.CRUDLessonDesignSection import CRUDLessonDesignSection
from app.edu.libs.Generator import Generator


class LessonsController:

    def generate_lesson(self, request):
        desc= request.form.get("desc")
        sections = request.form.getlist('sections')
        reportname = request.form.get('reportname')
        req_sections = []

        # Process the selected sections
        for section in sections:
            req_sections.append(section)

        generator = Generator()

        lesson_design = generator.generate_lesson_design(session['logger'], reportname, desc, req_sections)

        return render_template("lessons/lessondesign.html", lesson_design=lesson_design, desc=desc, reportname=reportname)

    def get_all_reports(self):
        crudlessondesign = CRUDLessonDesign()
        lessondesigns = crudlessondesign.retrieve_all(session['logger'])

        if len(lessondesigns) > 0:
            return render_template("lessons/myplans.html", lesson_designs=lessondesigns, reports_excit = 'Yes')

        return render_template("lessons/myplans.html", reports_excit='No')

    def get_report(self, report_id):
        crudlessondesign = CRUDLessonDesign()
        lessondesign = crudlessondesign.retrieve(report_id)

        crudlessondesignsection = CRUDLessonDesignSection()
        lessonsections = crudlessondesignsection.retrieve(lessondesign.id)


        # build plan details
        lesson_sections = {}
        for lessonsection in lessonsections:
            lesson_sections[lessonsection.lesson_design_section] = lessonsection.content

        return render_template("lessons/lessonview.html", lesson_sections=lesson_sections, desc=lessondesign.desc, reportname=lessondesign.lesson_design_name)


