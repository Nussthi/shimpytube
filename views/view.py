import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class View(Widget):
    """Class to display the view where the user is asked to put the video and destination folder

    Attributes
        controller : Controller
            Controller Object to manage the programm including the view

    Methods
        __init__(controller)
            Initialize the object with a controller
    """
    #Those lines retrive the user input on the kv file
    #Watch Tech with Tim - Kivy Tutorial
    youtubeURL = ObjectProperty(None)
    destinationFolder = ObjectProperty(None)

    def __init__(self,controller, **kwargs) -> None:
        super(View, self).__init__(**kwargs)
        #The view is created in the same time as the controller.
        #The idea is to initialize the view with a controller for further interactions.
        self.controller = controller
    
    def download_music(self):
        #Call the controller function to download the music
        self.controller.download_music(self.youtubeURL.text, self.destinationFolder.text)

    
class Shrimpytube(App):
    '''Class to display a GUI
        
        Attributes:
            controller : Controller Object
                Controller Object to manage the programm including the view

        Methods
            __init__(controller,**kwargs)
                Initialize the object with a controller    
        '''
    def __init__(self, controller=0, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = controller

    def build(self):
        return View(self.controller)
    