# Movie List Web Page

###Description: 
This project creates a webpage with information about movies, including the title, poster, and trailer.

###Installation: 
None necessary. Simply download the repository.

###How to use:
To generate the HTML and open the page, run 'entertainment_center.py'.

To add, remove, or update movies on the page, edit the instances of the class in 'entertainment_center.py'.
**NOTE**: The class instance must contain the following attributes:
	title (str): The movie's title.
	storyline (str): A brief summary or tagline describing the movie.
	poster_image_url (str): A URL for an image of the movie's poster.
	trailer_youtube_url (str): A URL for the movie's trailer on youtube.
	year_released (int): The year the movie was released in theaters
	rating (float): The movie's current rating on IMDB

To alter the sort order of the movies on the page, change the second parameter in open_movies_page

Available options include

* 'rating' - Sort in descending order by IMDB rating.
* 'year_released' - Sort in chronological order by release year.

