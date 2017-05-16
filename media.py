import webbrowser
#Declaring a class
class Movie():
    """"This class provides a way to store movie related information"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    # this is the first constructor for class Movie
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title #instance attribute of title
        self.storyline = movie_storyline#instance attribute of Storyline
        self.poster_image_url = poster_image#instance attribute of image
        self.trailer_youtube_url = trailer_youtube#instance attribute of trailer
    #Declaring instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
