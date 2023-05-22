

class NoFolderPathError(Exception):
    '''Path not provided'''

    def __init__(self, message="No folder path provided") -> str:
        self.message = message
        super().__init__(message)

    
class YoutubeURLError(Exception):
    '''Youtube URL not working'''

    def __init__(self, message="Youtube URL is not valid") -> str:
        self.message = message
        super().__init__(message)