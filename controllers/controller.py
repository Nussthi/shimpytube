import pytube
from views.view import Shrimpytube
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
        self.view = Shrimpytube(self)
        self.userPreferences = UserPreferences()

    def download_music(self, youtubeURL, destinationFolder):
        yt = pytube.YouTube(youtubeURL,use_oauth=True,allow_oauth_cache=True)

        streams = yt.streams.filter(only_audio=True)
        stream = streams[0]
        stream.download(destinationFolder)