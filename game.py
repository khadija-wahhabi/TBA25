# Description: Game class

# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms
        cour = Room("Cour", "dans la cour du château, entourée de hauts murs de pierre.")
        salle_trone = Room("Salle du trône", "dans la majestueuse salle du trône.")
        bibliotheque = Room("Bibliothèque", "dans une bibliothèque remplie de parchemins anciens.")
        cuisine = Room("Cuisine", "dans la cuisine du château, encore chaude.")
        chapelle = Room("Chapelle", "dans une chapelle silencieuse et solennelle.")
        donjon = Room("Donjon", "dans un donjon sombre et humide sous le château.")
        armurerie = Room("Armurerie", "dans l’armurerie remplie d’armes anciennes.")
        tour = Room("Tour", "au sommet de la tour du château, battue par le vent.")


        # Create exits for rooms
        cour.exits = {
            "N": salle_trone,
            "E": cuisine,
            "O": bibliotheque,
            "S": chapelle
        }

        salle_trone.exits = {
            "S": cour,
            "U": tour
        }

        bibliotheque.exits = {
            "E": cour
        }

        cuisine.exits = {
            "O": cour
        }

        chapelle.exits = {
            "N": cour,
            "D": donjon
        }

        donjon.exits = {
            "U": chapelle,
            "S": armurerie
        }

        armurerie.exits = {
            "N": donjon
        }

        tour.exits = {
            "D": salle_trone
        }

        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = cour

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
