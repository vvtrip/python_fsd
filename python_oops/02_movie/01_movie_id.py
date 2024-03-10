class Movie:
    
    id_counter = 1
    
    def __init__(self, title, rating):
        
        # assigning unique id to each class
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating
        
        # incrementing counter for the next class instance
        Movie.id_counter += 1

my_movie = Movie('Star Wars', 4)
your_movie = Movie('Godzilla', 5)

print(my_movie.id)
print(your_movie.id)

# prints 1 and 2