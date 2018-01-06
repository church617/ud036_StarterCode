import fresh_tomatoes
import media

# create each movie object and assign data
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")  # noqa

equilibrium = media.Movie("Equilibrium",
                          "Story of a mans rebuttal against tyranny",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Equilibriumposter.jpg/220px-Equilibriumposter.jpg",  # noqa
                          "https://www.youtube.com/watch?v=6IBNACePYk4")  # noqa

incredibles = media.Movie("Incredibles",
                          "A family of superheroes goes into retirement",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY5OTU0OTc2NV5BMl5BanBnXkFtZTcwMzU4MDcyMQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # noqa
                          "https://www.youtube.com/watch?v=eZbzbC9285I")  # noqa

kingdom_of_heaven = media.Movie("Kingdom of Heaven",
                                "A blacksmith gets a second chance at life"
                                "in the Holy City",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2MTIwNjg0MV5BMl5BanBnXkFtZTcwNjAxODIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                                "https://www.youtube.com/watch?v=Kfq9U2tWWGo")  # noqa

moana = media.Movie("Moana",
                    "A girl discovers why she likes the water",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")  # noqa

Star_Wars_Episode_1 = media.Movie("Star Wars: Episode 1",
                                  "A boy is found, and a new way of"
                                  "life begins",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/4/40/Star_Wars_Phantom_Menace_poster.jpg/220px-Star_Wars_Phantom_Menace_poster.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=bD7bpG-zDJQ")  # noqa
# pass all movie objects into a list to create the website
movies = [toy_story, equilibrium, incredibles, kingdom_of_heaven,
          moana, Star_Wars_Episode_1]
fresh_tomatoes.open_movies_page(movies)
# run open_movie_page method which creates HTML website
