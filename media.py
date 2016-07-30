import webbrowser

class Movie():
    """
    Attributes:
        title (str): The movie's title.
        storyline (str): A brief summary or tagline describing the movie.
        poster_image_url (str): A URL for an image of the movie's poster.
        trailer_youtube_url (str): A URL for the movie's trailer on youtube.
        year_released (int): The year the movie was released in theaters
        rating (float): The movie's current rating on IMDB
    """
        
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, year, rating):
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year_released = year
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
