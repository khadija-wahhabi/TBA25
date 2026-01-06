# Define the Player class.

from item import Item

class Player:
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

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
    
    # Define the move method.
    def move(self, direction):
        direction = direction.upper() 
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        
        if not self.history or self.history[-1] != self.current_room:
            self.history.append(self.current_room)

        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        if not self.history:
            return "Vous n'avez encore visité aucune pièce."
        s = "\nVous avez déjà visité les pièces suivantes:"
        for room in self.history:
            s += f"\n    - {room.name}"
        return s

    def back(self):
        if len(self.history) < 2:
            print("\nImpossible de revenir en arrière : aucune pièce précédente.\n")
            return False
        
        self.history.pop()
        
        self.current_room = self.history[-1]
        print(self.current_room.get_long_description())
        return True

    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        s = "\nVous disposez des items suivants :"
        for item in self.inventory.values():
            s += f"\n    - {item}" 
        return s

    def take(self, item_name):
        item = self.current_room.remove_item(item_name)
        if item:
            self.inventory[item.name] = item
            print(f"Vous avez pris l'objet '{item.name}'.")
        else:
            print(f"Impossible de prendre '{item_name}' : objet absent de la pièce.")


    def drop(self, item_name):
        item = self.inventory.pop(item_name, None)
        if item:
            self.current_room.add_item(item)
            print(f"Vous avez déposé l'objet '{item.name}'.")
        else:
            print(f"Impossible de déposer '{item_name}' : objet absent de l'inventaire.")

