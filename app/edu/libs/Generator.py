import openai

from app.edu.constants.Phrases import Phrases
from app.edu.constants.k import F, S, T
from app.edu.database.crud.CRUDLessonDesignSection import CRUDLessonDesignSection
from app.edu.database.utils.Helper import Helper
from app.edu.errorhandlers.GeneralHandler import GeneralHandler
from app.edu.database.crud.CRUDLessonDesign import CRUDLessonDesign

class Generator:
    LESSON_OUTLINE = ['Objectives', 'Lesson Duration',  'Required Materials', 'Lesson Outline', 'PowerPoint Slides', 'Interactive '
                                                                                                 'Activities',
                      'Conclusion']

    def generate_lesson_design(self, user_id, reportname, user_text, req_sections):
        oak = "{0}{1}{2}".format(F, S, T)
        lesson_design_id = Helper.generate_random_string(14)

        # Add leasson
        lesson = {'id': lesson_design_id,
                         'lesson_design_name': reportname,
                         'desc': user_text,
                         'user_id': user_id
                         }
        crudlessondesign = CRUDLessonDesign()
        addlessondesign = crudlessondesign.add(lesson)

        # generate sections
        lesson_design_sections = []
        lesson_design = {}
        for i in range(len(req_sections)):
            lesson_outline = self._generate_lesson_outline(oak, user_text, req_sections[i])
            lesson_design[req_sections[i]] = lesson_outline
            lesson_design_sections.append({
                'id': Helper.generate_random_string(14),
                'lesson_design_section': req_sections[i],
                'content': lesson_outline,
                'lesson_design_id': lesson_design_id
            })

        # Add lesson design sections
        crudlessondesignsection = CRUDLessonDesignSection()
        addlessondesignsections = crudlessondesignsection.bulk_add(lesson_design_sections)

        return lesson_design

    def _generate_lesson_outline(self, oak, user_text, outline):
        try:
            openai.api_key = oak
            # Define the GPT-3 prompt that will be used to generate rephrased paragraphs
            text = Phrases.CREATE_LESSON_DESIGN_ORDER.format(outline, user_text)
            prompt = (text)
            # Define the OpenAI API parameters
            parameters = {
                "model": "text-davinci-003",
                "prompt": prompt,
                "temperature": 0.7,
                "max_tokens": 4000,
                "top_p": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0

            }

            # Call the OpenAI API to generate paragraphs
            response = openai.Completion.create(**parameters)

            lesson_design = response.choices[0].text.strip()
            lesson_design = self.format_response(lesson_design)

            return lesson_design

        except Exception as e:
            generalhandler = GeneralHandler()
            return generalhandler.general_error('500', e)

    def format_response(self, response):
        # Replace newline characters with line breaks for HTML rendering
        response = response.replace('\n', '<br>')

        # Format lists as bulleted points
        response = response.replace('- ', '• ')

        # Format titles with a larger font size or other styling
        # response = f'<h2>{response}</h2>'

        return response
