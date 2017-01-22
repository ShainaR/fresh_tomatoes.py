import fresh_tomatoes
import media

#Toy Story instance
toy_story = media.Movie("Toy Story",
                        "Andy's toys come to life",
                        "81 minutes",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#Avatar instance
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "162 minutes",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#Braveheart instance
braveheart = media.Movie("Braveheart",
                         "One Scottish rebel takes on the English to avenge his love and set his people free",
                         "182 minutes",
                         "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=wj0I8xVTV18&spfreload=10")

#The Village instance
the_village = media.Movie("The Village",
                          "A village is plagued by monsters in the forest, but is faced with a dark secret when a blind girl is forced to leave for medicine in the towns.",
                          "109 minutes",
                          "https://upload.wikimedia.org/wikipedia/en/a/a0/The_Village_movie.jpg",
                          "https://www.youtube.com/watch?v=lwq4oTboRi4")

#Breakfast Club instance
the_breakfast_club = media.Movie("The Breakfast Club",
                                 "Five high school students from different walks of life are forced to relate during a one day school detention.",
                                 "97 minutes",
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/The_Breakfast_Club.jpg/220px-The_Breakfast_Club.jpg",
                                 "https://www.youtube.com/watch?v=BSXBvor47Zs")

#Heathers instance
heathers = media.Movie("Heathers",
                        "Three wealthy and popular high school girls, all named Heather, are brought down by Veronica Sawyer and her psychotic murderous boyfriend.",
                        "103 minutes",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/Heathersposter89.jpg/220px-Heathersposter89.jpg",
                        "https://www.youtube.com/watch?v=3Yl_eZ6Iem8")


movies = [toy_story, avatar, braveheart, the_village, the_breakfast_club, heathers]
fresh_tomatoes.open_movies_page(movies)

