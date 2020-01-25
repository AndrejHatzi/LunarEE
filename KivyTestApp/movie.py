"""..."""


# TODO: Create your Movie class in this file


class Movie:
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched
    def __str__(self):
        return ('{},{},{},{}'.format(self.title, self.year, self.category, self.is_watched))

#sw = Movie("SW", 1977, "action", 0);
#print(sw);
