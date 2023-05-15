
class UserPreferences:
    '''Class to manage user preferences

    Attributes
        destinationFolder: str
            A string to memorize the user destination folder

    '''
    def __init__(self) -> None:
        self.destinationFolder = ""

    def set_destination_folder(self, destinationFolder):
        self.destinationFolder = destinationFolder

    def get_destination_folder(self):
        return self.destinationFolder