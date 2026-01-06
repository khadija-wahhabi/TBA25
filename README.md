# TBA25
classDiagram
    class Game {
        - bool finished
        - list rooms
        - dict commands
        - Player player
        + __init__()
        + setup()
        + play()
        + process_command(command)
        + print_welcome()
    }

    Game --> Player
    Game --> Room
    Game --> Command
    Command --> Actions
