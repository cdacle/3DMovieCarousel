""" 
Movie class

"""
import webbrowser

class Movie:
    """
    Movie class has the following fields.

    title:        movie title
    description:  short description
    poster:       poster image url 
    trailer:      youtube url
    imdb_rating:  imdb score
    release:      year of release
    mpaa_rating:  rating by the motion picture assoc. of america
    director:     name(s) of director(s)
    stars:        actors/actresses 
    """

    def __init__(self, title, description, poster, trailer, imdb_rating, release, mpaa_rating, director, stars):
        """ initialization with individual arguments """

        self.title = title
        self.description = description
        self.poster = poster
        self.trailer = trailer
        self.imdb_rating = imdb_rating
        self.release = release
        self.mpaa_rating = mpaa_rating
        self.director = director
        self.stars = stars


    def __init__(self, movie_data):
        """ initialization from dictionary """

        if ("title" in movie_data):
            self.title = movie_data["title"]

        if ("description" in movie_data):
            self.description = movie_data["description"]

        if ("poster" in movie_data):
            self.poster = movie_data["poster"]

        if ("trailer" in movie_data):
            self.trailer = movie_data["trailer"]

        if ("imdb_rating" in movie_data):
            self.imdb_rating = movie_data["imdb_rating"]

        if ("release" in movie_data):
            self.release = movie_data["release"]

        if ("mpaa_rating" in movie_data):
            self.mpaa_rating = movie_data["mpaa_rating"]

        if ("director" in movie_data):
            self.director = movie_data["director"]

        if ("stars" in movie_data):
            self.stars = movie_data["stars"]


    def show_trailer(self):
        """ Show trailer in the browser """

        webbrowser.open(self.trailer_youtube_url)


    def pretty_print(self):
        """ dump the object to console """

        print("-----------------------------")
        print(self.title)
        print(" --- " + self.description)
        print("")
        print("Release: " + self.release)
        print("MPAA rating: " + self.mpaa_rating)
        print("Director: " + self.director)
        print("Stars: " + self.stars)
        print("")
        print("poster: " + self.poster)
        print("trailer: " + self.trailer)
        print("IMDB rating: " + self.imdb_rating)


