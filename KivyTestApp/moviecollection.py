"""..."""
from movie import Movie
from operator import itemgetter
# TODO: Create your MovieCollection class in this file


class MovieCollection:
    def __init__(self):
        self.movies = []

    def __str__(self):
        return ("movie => {}".format(self.movies))

    def load_movies(self, moviesFile):
        with open(moviesFile, "r") as f:
            fmovies = f.readlines()
        for m in range(len(fmovies)):
            if (fmovies[m] not in self.movies):
                self.movies.append(fmovies[m])
        #self.movies += (fmovies)
        return(self.movies)

    def add_movie(self, movieObjects):
        currentMovie = str(movieObjects)
        currentMovie = currentMovie.split(",")
        
        if (currentMovie[-1] == str(True)):
            currentMovie[-1] = "w\n"
            currentMovie = ",".join(currentMovie)
            self.movies.append(currentMovie)

        if (currentMovie[-1] == str(False)):
            currentMovie[-1] = "u\n"
            currentMovie = ",".join(currentMovie)
            self.movies.append(currentMovie)

    def unwatchedMovies(self):
        u = 0
        for m in range(len(self.movies)):
            if(self.movies[m].split(",")[-1].replace("\n", "") == "u"):
                u += 1
        return (u)

    def watchedMovies(self):
        w = 0
        for m in range(len(self.movies)):
            if(self.movies[m].split(",")[-1].replace("\n", "") == "w"):
                w += 1
        return (w) 
    
    def sort(self, type):
        if type == "year":
            sortedList = []
            yearIndex = []
            for y in range(len(self.movies)):
                yearIndex.append((y, int(self.movies[y].split(",")[1])))
            yearIndex.sort(key=itemgetter(1), reverse=True)
            for y in range(len(self.movies)):
                sortedList.append(self.movies[yearIndex[y][0]])
            self.movies = sortedList
            print(self.movies)
        if type == "title":
            sortedList = []
            titleIndex = []
            for t in range(len(self.movies)):
                titleIndex.append((t, self.movies[t].split(",")[0].split(" ")[0][0]))
            
            titleIndex.sort(key=itemgetter(1))
            #print(titleIndex)
            for t in range(len(self.movies)):
                sortedList.append(self.movies[titleIndex[t][0]])
            self.movies = sortedList
            print(self.movies)
    
    def save_movies(self):
        #print(self.movies)
        with open("movies.csv", "r") as f:
            fmovies = f.readlines()
        for m in range(len(self.movies)):
            if (self.movies[m] not in fmovies):
                with open("movies.csv", "a") as f:
                    f.write("{}".format(self.movies[m]))

            
            

#MovieCollection.add_movie(Movie("Amazing Grace", 2006, "Drama", False));
#print(MovieCollection.movies);

#MovieCollection.load_movies("movies.csv")

#MovieCollection().load_movies("movies.csv")
#print()

#y = MovieCollection()
#y.add_movie(Movie("Wars Upon", 1977, "Action", False))
#y.load_movies("movies.csv")
#y.sort("title")
#y.watchedMovies()
#print(y.unwatchedMovies())
#print(w)