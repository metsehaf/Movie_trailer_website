import media # import media module/file
import fresh_tomatoes # import fresh_tomatoes python file
#Instaniate class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock",
                     "Storyline",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouile = media.Movie("Ratatouille",
                     "Storyline",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                     "Storyline",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games",
                     "Storyline",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=mfmrPu43DF8")
# Calling movie class on instances
movies = [toy_story, avatar, school_of_rock, ratatouile, midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)#open movie page method



