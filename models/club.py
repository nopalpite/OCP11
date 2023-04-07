class Club:
    def __init__(self, name, email, points):
        self.name = name
        self.email = email
        self.points = int(points)

    def __eq__(self, other):
        if isinstance(other, Club):
            return self.name == other.name and self.email == other.email and self.points == other.points
        return False
