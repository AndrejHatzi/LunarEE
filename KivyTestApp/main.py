# def __init__(self, title="", year=0, category="", is_watched=False):
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from movie import Movie
from moviecollection import MovieCollection
from time import sleep

movCollec = MovieCollection()

class MyBoxLayout(BoxLayout):

    movCollec.load_movies("movies.csv")
    title = ObjectProperty(None)
    year = ObjectProperty(None)
    category = ObjectProperty(None)
    
    def addMovie(self):
        """
        This method retrieves data stored in TextInputs
        """
        #watched = True
        print(self.title.text, self.year.text, self.category.text, self.is_watched.active)

        #if (self.is_watched.active):
        #    watched = True
        #else:
        #    watched = False
        if ((len(self.title.text) <= 0) or (len(self.year.text) <= 0) or (len(self.category.text))<=0):
            popup = Popup(title='Alert',
            content=Label(text="Please complete the form"),
            size_hint=(None, None), size=(400, 400))
            popup.open()
        else:
            movCollec.add_movie(Movie(self.title.text,self.year.text,self.category.text,self.is_watched.active))
            self.title.text = ""
            self.year.text = ""
            self.category.text = ""
            popup = Popup(title='Add movie',
            content=Label(text='{} added to movie list'.format(self.title.text)),
            size_hint=(None, None), size=(400, 400))
            popup.open()
        
        

    def SaveMovies(self):
        movCollec.save_movies()
        popup = Popup(title='Save movies',
        content=Label(text='Movies saved to file'),
        size_hint=(None, None), size=(400, 400))
        popup.open()

    def nWatchedMovies(self):
        popup = Popup(title='Watched movies',
        content=Label(text="{} unwatched".format(movCollec.watchedMovies())),
        size_hint=(None, None), size=(400, 400))
        popup.open()

    def nUnwatchedMovies(self):
        popup = Popup(title='unwatched movies',
        content=Label(text="{} unwatched".format(movCollec.unwatchedMovies())),
        size_hint=(None, None), size=(400, 400))
        popup.open()

    def SortTitle(self):
        #print(movCollec)
        print(movCollec.sort("title"))
        popup = Popup(title='Sort by Title',
        content=Label(text="Look at the console!"),
        size_hint=(None, None), size=(400, 400))
        popup.open()
    
    def SortYear(self):
        print(movCollec.sort("year"))
        #print(y)
        popup = Popup(title='Sort by Year',
        content=Label(text="Look at the console!"),
        size_hint=(None, None), size=(400, 400))
        popup.open()
        
class MoviesToWatchApp(App):
    def build(self):
        return MyBoxLayout() 
   


if __name__ == '__main__':
    MoviesToWatchApp().run()
