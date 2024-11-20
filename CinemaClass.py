class Cinema:
    def __init__(self):
        self.movies={}

    def add_move(self,movie,seats):
        if movie in self.movies:
            print(f"Movie {movie} is already in the system.")
        else:
            self.movies[movie]={'seats' : seats, 'sold' : 0}
            print(f"Movie {movie} added with {seats} available seats.")

    def sell_ticket(self,movie):
        if movie not in self.movies:
            print(f"Movie {movie} is not in the system.")
        else:
            if self.movies[movie]['seats']>0:
                self.movies[movie]['seats']-=1
                self.movies[movie]['sold']+=1
                print(f"Ticket sold for movie {movie}. {self.movies[movie]['seats']} seats remaining.")
            else:
                print(f"No available seats for movie {movie}.")

    def cancel_ticket(self,movie):
        if movie not in self.movies:
            print(f"Movie {movie} is not in the system.")
        else:
            if self.movies[movie]['sold']>0:
                self.movies[movie]['seats']+=1
                self.movies[movie]['sold']-=1
                print(f"Ticket canceled for movie {movie}. {self.movies[movie]['seats']} seats available.")
            else:
                print(f"No ticket sold for movie {movie}.")

    def get_available_seats(self,movie):
        if movie not in self.movies:
            print(f"Movie {movie} not in the system.")
        else:
            return self.movies[movie]['seats']

    def list_movies(self):
        if not self.movies:
            print("No movies are being screened at the moment.")
        else:
            print("Movies currently being screened:")
            for movie in self.movies:
                print(f"- {movie} ({self.movies[movie]['seats']} seats available)")

    def get_ticket_sales(self,movie):
        if movie not in self.movies:
            print(f"Movie {movie} is not in the system.")
        else:
            return self.movies[movie]['sold']


cinema=Cinema()
cinema.add_move("Avatar",100)
cinema.add_move("The dark knight",50)
cinema.sell_ticket("Avatar")
cinema.sell_ticket("The dark knight")
cinema.cancel_ticket("Avatar")
cinema.list_movies()
print(f"Ticket sold for Avatar : {cinema.get_ticket_sales('Avatar')}")
print(f"Tickets sold for The dark knight : {cinema.get_ticket_sales('The dark knight')}")
