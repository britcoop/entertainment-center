import webbrowser

class Movie():
	""" This class provides a way to store movie related information """

	#this is 'blueprint' from which all movie instances are based
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	#opens the webbrowser and goes to the url indiciated in the instance
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)