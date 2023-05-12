class View:
    """Class to display information to the user

    Attributes
        controller : Controller
            Controller Object to manage the programm including the view

    Methods
        __init__(controller)
            Initialize the object with a controller
    """

    def __init__(self,controller) -> None:
        #The view is created in the same time as the controller.
        #The idea is to initialize the view with a controller for further interactions.
        self.controller = controller

    def ask_url(self) -> None:
        url = input("Enter the URL : ")
        print(url)

    def ask_destination_folder(self) -> None:
        destinationFolder = input("Enter the destination folder : ")
        print(destinationFolder)