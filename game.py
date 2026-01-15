# Description: Game class

# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

DEBUG = False

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.quests = {
            "item_parchemin": False,
            "reach_tour": False,
            "talk_bibliothecaire": False }

    
    # Setup the game
    def setup(self):

        # Setup commands
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : observer la pièce et voir les items présents", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <item> : prendre un item présent dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <item> : déposer un item dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : vérifier l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk", " <personnage> : parler à un personnage", Actions.talk, 1)
        self.commands["talk"] = talk
        talk = Command("talk", " <pnj> : parler à un personnage", Actions.talk, 1)
        self.commands["talk"] = talk


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

        # Setup items in rooms
        cour.add_item(Item("pierre", "une pierre ronde et lourde", 2))
        cour.add_item(Item("torche", "une torche en bois, non allumée", 1))

        salle_trone.add_item(Item("couronne", "une couronne dorée ornée de pierres", 1))
        salle_trone.add_item(Item("sceptre", "un sceptre royal en métal", 2))

        bibliotheque.add_item(Item("livre", "un livre ancien couvert de poussière", 1))
        bibliotheque.add_item(Item("parchemin", "un parchemin jauni", 0.5))

        cuisine.add_item(Item("couteau", "un couteau de cuisine bien aiguisé", 1))
        cuisine.add_item(Item("pain", "un pain encore tiède", 0.5))

        chapelle.add_item(Item("chandelier", "un chandelier en bronze", 2))

        donjon.add_item(Item("chaine", "une chaîne en fer rouillée", 3))

        armurerie.add_item(Item("epee", "une épée au fil tranchant", 3))
        armurerie.add_item(Item("bouclier", "un bouclier solide", 4))

        tour.add_item(Item("longuevue", "une longue-vue ancienne", 1))

        #Setup characters in rooms
        garde = Character("Garde", "un garde fatigué qui surveille l'entrée", cour,
            ["Halte ! Personne ne passe sans autorisation."])

        bibliothecaire = Character("Bibliothécaire", "une vieille dame qui murmure des secrets", bibliotheque,
            ["Chut... certains livres ne doivent pas être ouverts."])

        forgeron = Character("Forgeron", "un forgeron couvert de suie", armurerie,
            ["Ces armes n’attendent qu’un héros digne."])

        # Ajouter les PNJ aux rooms
        cour.add_character(garde)
        bibliotheque.add_character(bibliothecaire)
        armurerie.add_character(forgeron)

        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = cour
        self.player.history.append(self.player.current_room)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()

        while not self.finished:
            self.process_command(input("> "))

            if self.win():
                print("\n🎉 Bravo ! Vous avez complété toutes les quêtes. Vous avez gagné !\n")
                self.finished = True
                continue

            if self.loose():
                print("\n💀 Vous avez perdu… Entrer dans le donjon sans torche était une mauvaise idée.\n")
                self.finished = True
                continue

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.strip().split()
        if not list_of_words:
            return

        command_word = list_of_words[0].lower()

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{list_of_words[0]}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            return

        command = self.commands[command_word]
        command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())

    def move_characters(self):
        all_chars = []
        for room in self.rooms:
            all_chars.extend(list(room.characters.values()))
        for c in all_chars:
            c.move()

    def on_take(self, item_name: str):
        if item_name.lower() == "parchemin":
            self.quests["item_parchemin"] = True

    def on_move(self):
        if self.player.current_room.name.lower() == "tour":
            self.quests["reach_tour"] = True

    def on_talk(self, character_name: str):
        if character_name.lower() == "bibliothécaire" or character_name.lower() == "bibliothecaire":
            self.quests["talk_bibliothecaire"] = True

    def win(self) -> bool:
        return all(self.quests.values())

    def loose(self) -> bool:
        if self.player.current_room.name.lower() == "donjon":
            has_torch = "torche" in self.player.inventory
            return not has_torch
        return False
        
def main():
    # Create a game object and play the game
    Game().play()

if __name__ == "__main__":
    main()
