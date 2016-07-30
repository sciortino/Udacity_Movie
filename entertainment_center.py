import media
import fresh_tomatoes

#Optional - Unhide next line to display Movie class documentation
#print media.Movie.__doc__

#Create instances of the Movie class
godfather = media.Movie(
    'The Godfather',
    'The Corleone family is up to their old antics.',
    'http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
    'http://www.youtube.com/watch?v=sY1S34973zA',
    1972,
    9.2)

blood = media.Movie(
    "There Will Be Blood",
    "An oiling operation goes all wrong, for some.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/d/da/There_Will_Be_Blood_Poster.jpg/220px-There_Will_Be_Blood_Poster.jpg", #NOQA
    "http://www.youtube.com/watch?v=FeSLPELpMeM",
    2007,
    8.1)

lebowski = media.Movie(
    "The Big Lebowski",
    "A bowling movie.",
    "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
    "http://www.youtube.com/watch?v=cd-go0oBF4Y",
    1998,
    8.2)

starwars = media.Movie(
    "Star Wars",
    "The rebels take on the Empire.",
    "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
    "http://www.youtube.com/watch?v=1g3_CFmnU7k",
    1977,
    8.7)

graduate = media.Movie(
    "The Graduate",
    "A recent college graduate gets attention from an older woman.",
    "http://upload.wikimedia.org/wikipedia/en/8/8b/Graduateposter67.jpg",
    "http://www.youtube.com/watch?v=XxJDOkr_UhE",
    1967,
    8.0)

blues = media.Movie(
    "Blues Brothers",
    "This band is on a mission from God.",
    "http://upload.wikimedia.org/wikipedia/en/a/ae/Bluesbrothersmovieposter.jpg",
    "http://www.youtube.com/watch?v=asM2-YAMWxg",
    1980,
    7.9)

#Pass movies into a list and open the movie page.

movies = [godfather, blood, lebowski, starwars, graduate, blues]
fresh_tomatoes.open_movies_page(movies)
