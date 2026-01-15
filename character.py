# Description: Character class

import random
try:
    from game import DEBUG
except ImportError:
    DEBUG = False


class Character:
    """
    Classe représentant un personnage non joueur (PNJ).

    Attributs:
        name (str): le nom du personnage
        description (str): la description du personnage
        current_room (Room): la pièce où se trouve le personnage
        msgs (list[str]): liste de messages que le personnage peut dire
    """
    
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs[:]
        self._msg_index = 0 

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        if not self.msgs:
            return ""

        msg = self.msgs[self._msg_index]
        self._msg_index = (self._msg_index + 1) % len(self.msgs)
        return msg

    def move(self):
        if random.choice([True, False]) is False:
            return False

        next_rooms = [room for room in self.current_room.exits.values() if room is not None]
        if not next_rooms:
            return False

        old_room = self.current_room
        new_room = random.choice(next_rooms)

        old_room.remove_character(self.name.lower())

        new_room.add_character(self)

        if DEBUG:
            print(f"DEBUG: {self.name} se déplace de {old_room.name} vers {new_room.name}")

        return True
