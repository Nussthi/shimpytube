from configparser import ConfigParser
from models.custom_exceptions import NoFolderPathError

class UserPreferences:
    '''Class to manage user preferences

    Attributes
        destinationFolder: str
            A string to memorize the user destination folder

    '''
    def __init__(self) -> None:
        self.config = ConfigParser()

    def set_destination_folder(self, destination_folder) -> None:
        '''Set the user destination folder in the .ini file

        Parameters:
            destination_folder : str
                the path of the desired folder
        
        Return
            None
        '''
        #If no folder path is provided, raise an Error
        if destination_folder == "":
            raise NoFolderPathError()

        #If the .ini file doesn't exist, we create it
        if self.check_file_exist() == False:
            self.make_config_file()

        #Write the path in the .ini file
        with open("user_preferences.ini", "w",encoding="utf-8") as file:
            self.config["DEFAULT"]["destinationfolder"] = destination_folder
            self.config.write(file)
        

    def get_destination_folder(self) -> str:
        '''get the user destination folder in the .ini file

        Parameters:
            None
        
        Return
            destinationFolder : str
                the path to the folder
        '''
        destinationFolder = ""

        try:
            self.config.read("user_preferences.ini")
            destinationFolder = self.config["DEFAULT"]["destinationfolder"]
        except KeyError:
            pass

        if destinationFolder != "":
            return destinationFolder
        
        return ""
    
    def make_config_file(self) -> None:
        '''Create a config file that will contain user preferences

        Parameters:
            None
        
        Return
            None
        '''
        #create a default config with no path
        self.config["DEFAULT"] = {
            "destinationfolder":""
        }

        with open("user_preferences.ini", "w",encoding="utf-8") as file:
            self.config.write(file)

    def check_file_exist(self) -> bool:
        '''Check if the config file exist

        Parameters:
            None

        Return
            bool
        '''
        #Return true if "..." or false if ""
        return bool(self.config.read("user_preferences.ini"))