import webbrowser


class Director():
    """ This class provides a way to store director information"""

    def __init__(
            self,
            director_name,
            director_birthplace,
            director_hairstyle,
            director_items_of_note):
        self.name = director_name
        self.birthplace = director_birthplace
        self.hair_style = director_hairstyle
        self.items_of_note = director_items_of_note
