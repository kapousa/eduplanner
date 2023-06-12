import openai

from app.edu.constants.Phrases import Phrases
from app.edu.constants.k import F, S, T


class Generator:
    LESSON_OUTLINE = ['Objectives', 'Lesson Duration',  'Required Materials', 'Lesson Outline', 'PowerPoint Slides', 'Interactive '
                                                                                                 'Activities',
                      'Conclusion']

    def generate_lesson_design(self, user_text):
        oak = "{0}{1}{2}".format(F, S, T)

        lesson_design = {}

        for i in range(len(self.LESSON_OUTLINE)):
            lesson_outline = self._generate_lesson_outline(oak, user_text, self.LESSON_OUTLINE[i])
            lesson_design[self.LESSON_OUTLINE[i]]  = lesson_outline

        # Print the rephrased paragraphs
        return lesson_design

    def _generate_lesson_outline(self, oak, user_text, outline):
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
        # lesson_design = html.escape(lesson_design)

        # Extract the paragraphs from the OpenAI API response
        # lesson_design = response.choices[0].text

        # Clean up the paragraphs
        # lesson_design = re.sub('\n', '<p>', lesson_design)
        # lesson_design = re.sub('\t', '<p><p><li>', lesson_design)

        # Print the rephrased paragraphs
        return lesson_design

    def format_response(self, response):
        # Replace newline characters with line breaks for HTML rendering
        response = response.replace('\n', '<br>')

        # Format lists as bulleted points
        response = response.replace('- ', '• ')

        # Format titles with a larger font size or other styling
        # response = f'<h2>{response}</h2>'

        return response
