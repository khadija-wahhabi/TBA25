# Define the Player class.
    """
    This class represents the player in the game.
    The player has a name and is always located in one room at a time.

    Attributes:
        name (str): The name of the player.
        current_room (Room): The room where the player is currently located.

    Methods:
        __init__(self, name): Initializes the player with a name.
        move(self, direction): Moves the player to another room according to a direction.

    Examples:
        >>> from player import Player
        >>> player = Player("Indiana")
        >>> player.name
        'Indiana'
    """

class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    
