""" Media module used to create movie instanes """


class Movie():
    """This class accepts four arguments for our movie page:
        * Movie title
        * Storyline
        * Poster image
        * Yourtube trailer
    """

    # constructor
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        # sets movie properties
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
