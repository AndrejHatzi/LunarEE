
from operator import itemgetter
from movie import Movie
from moviecollection import MovieCollection
from time import sleep

movCollec = MovieCollection()

class mainProgram(MovieCollection):
    
    def __init__(self):
        pass

    def menu(self):
        print("Movies To Watch 2.0 - by Chaisrakeo Nathas ")
        print(len(movCollec.load_movies("movies.csv")), "Movies loaded")
        print("(1) Add Movie")
        print("(2) Number of watched movies")
        print("(3) Numer of unwatched movies")
        print("(4) Sort by Year")
        print("(5) Sort by Title")
        print("(6) Save Movies")
        print("(7) Exit")

    def addMovie(self):
        title = input("Title: ")
        while (len(title) <= 0):
            print("Input can not be blank")
            addMovie()
        year = input("Year: ")
        while (len(year) <= 0):
            print("Invalid input; enter a valid number")
        category = input("Category: ")
        while (len(category) <= 0):
            print("Input can not be blank")
        seen = 2
        while((seen != 1) or (seen != 0)):

            seen = int(input("[1]Watched [2]Unwatched: "))
            if (seen == 1):
                seen = True
                break
            elif(seen == 2):
                seen = False
                break
        movCollec.add_movie(Movie(title,year,category,bool(seen)))
        print(title, "added to movie list")
        sleep(3)

    def main(self):
        k = 1
        
        while (k != 7):
            self.menu()
            #print(movCollec)
            k = int(input(">"))
            if (k == 1):
                self.addMovie()
            elif (k == 2):
                print("{} watched".format(movCollec.watchedMovies()))
                sleep(3)
            elif (k == 3):
                print("{} unwatched".format(movCollec.unwatchedMovies()))
                sleep(3)
            elif (k == 4):
                movCollec.sort("year")
            elif (k == 5):
                movCollec.sort("title")
            elif (k == 6):
                movCollec.save_movies()
                print("Movies saved to file")
                
if __name__ == '__main__':
    mainProgram().main()
