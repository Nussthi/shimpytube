import pytube
from views.view import View
from models.userpreferences import UserPreferences

class Controller:
    '''Class to manage the operation of the program

    Attributes
        view : View
            An Object View to display information to the user

    Methods
        __init__
    '''
    def __init__(self) -> None:
        self.view = View(self)
        self.userPreferences = UserPreferences()

    def downloadMusic(self):
        videoURL = self.view.ask_url()
        destinationFolder = self.view.ask_destination_folder()
        yt = pytube.YouTube(videoURL,use_oauth=True,allow_oauth_cache=True)

        streams = yt.streams.filter(only_audio=True)
        stream = streams[0]
        stream.download(destinationFolder)