import pytube
import re
from views.view import Shrimpytube
from models.userpreferences import UserPreferences
from models.custom_exceptions import NoFolderPathError
from models.custom_exceptions import YoutubeURLError

class Controller:
    '''Class to manage the operation of the program

    Attributes
        view : View
            An Object View to display information to the user

    Methods
        __init__
    '''
    def __init__(self) -> None:
        self.app = Shrimpytube(self)
        self.userPreferences = UserPreferences()

    def download_music(self, youtube_url, destination_folder) -> None:
        '''Download the audio of the youtube video

        Parameters
            youtube_url : str
                The link of the youtube video
            destination_folder : str
                The folder path to save the audio

        Return
            None
        '''
        #If the folder path is not provided, we check in the .ini file
        if destination_folder == "":
            try:
                destination_folder = self.get_destination_folder()
            except KeyError:
                raise NoFolderPathError

        #Checking if the youtube url is valid        
        youtube_url_state = self.verify_youtube_url(youtube_url)
        if youtube_url_state is False:
            raise YoutubeURLError

        #Downloading the audio of the youtube video
        yt = pytube.YouTube(youtube_url,use_oauth=True,allow_oauth_cache=True)

        streams = yt.streams.filter(only_audio=True)
        stream = streams[0]
        stream.download(destination_folder)

    def verify_youtube_url(self, youtube_url) -> bool:
        '''Verify if the URL is a youtube url

        Parameters
            youtube_url : str
                The URL to verify

        Return
            A boolean wether the comparison is good or not
        '''
        regexYoutubeURL = r"^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?$"

        match = re.search(regexYoutubeURL, youtube_url)

        if match is not None :
            return True
        
        return False

    def save_user_preferences(self, destination_folder):
        '''Save the destination folder in a .ini file

        Parameters
            destination_folder : str
                folder path to save

        Return
            None
        '''
        try:
            self.userPreferences.set_destination_folder(destination_folder)
        except NoFolderPathError:
            raise NoFolderPathError
        
    def get_destination_folder(self) -> str:
        '''Return the user destination folder
        '''
        return self.userPreferences.get_destination_folder()