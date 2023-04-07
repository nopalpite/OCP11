class Competition:
    def __init__(self, name, date, number_of_places):
        self.name = name
        self.date = date
        self.number_of_places = int(number_of_places)

    def __eq__(self, other):
        if isinstance(other, Competition):
            return self.name == other.name and self.date == other.date and self.number_of_places == other.number_of_places
        return False