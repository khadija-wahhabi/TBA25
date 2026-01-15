# Description: Character class

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

