from views.view import View

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

    def say_hello(self) -> None:
        print("Hello")
