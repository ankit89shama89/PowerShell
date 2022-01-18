class Movies:
    def __init__(self, movie_name, movie_director):
        self.name = movie_name
        self.director = movie_director
    def print_info(self):
        print(f"<<{self.name}>> by {self.director} ")

movie1 = Movies('Kaddka','Ramgopal')

print(movie1.director)

movie1.print_info()



round(19.456456)
