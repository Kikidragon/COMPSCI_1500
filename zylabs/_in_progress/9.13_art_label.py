#FIXME unfinished
class Artist:
    def __init__(self, name=None, birth_year=0, death_year=0):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    # Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)

    def print_info(self):
        if self.death_year == -1:
            print("Artist: {} ({})".format(self.name, self.birth_year))
        else:
            print("Artist: {} ({}-{})".format(self.name, self.birth_year, self.death_year))

    # Define print_info() method. If death_year is -1, only print birth_year


class Artwork:
    def __init__(self, title=None, year_created=0, artist=None):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    # Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)

    def print_info(self):
        Artist.print_info()
        print("Title: {}, {}".format(self.title, self.year_created))

    # Define print_info() method


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()
