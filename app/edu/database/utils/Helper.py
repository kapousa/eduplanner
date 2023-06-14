import random
import string


class Helper:

    @staticmethod
    def generate_random_string(length):
        characters = string.ascii_uppercase + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string