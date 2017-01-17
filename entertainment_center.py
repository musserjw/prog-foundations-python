"""This is the Entertainment Center which is used to create instances of
    the Media class with our favorite movies.
"""

import fresh_tomatoes
import media

#Creation of instances for each movie
toyStory = media.Movie("Toy Story",
                       "toys come to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
starWars = media.Movie("Star Wars",
                       "A galaxy far, far, away",
                       "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                       "https://www.youtube.com/watch?v=sC9abcLLQpI")
talledegaNights = media.Movie("Talledega Nights",
                              "Comedy of a Nascar Driver",
                              "https://upload.wikimedia.org/wikipedia/en/e/e7/Talladega_nights.jpg",
                              "https://www.youtube.com/watch?v=Xe1rV0qLPJs")
gladiator = media.Movie("Gladiator",
                        "Slave becomes hero",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")
terminator = media.Movie("The Terminator",
                         "Robot travels from future",
                         "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
                         "https://www.youtube.com/watch?v=feH8GKqRccU")

#creates list of movies to be processed by fresh tomatoes
movies = [toyStory, avatar, starWars, talledegaNights, gladiator, terminator]

#calls fresh tomatoes which loads the webpage
fresh_tomatoes.open_movies_page(movies)
