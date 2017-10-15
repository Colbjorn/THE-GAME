# This module deals with actions that the player can take.
# Tracked separately from stats in order to not create mutual dependencies.
from map import room
from player_stats import player_location


def move(direction):
    # Moves player's location by one unit in a given direction, and erases player from previous location.
    room[player_location[1]][player_location[0]] = "#"
    # TODO: Make a valid exit check in order to avoid any errors.
    if direction == "south":
        player_location[1] += 1
    elif direction == "north":
        player_location[1] -= 1
    elif direction == "west":
        player_location[0] -= 1
    elif direction == "east":
        player_location[0] += 1


from room_generator import print_room, update_room


print_room(room)
update_room(room)
move("west")
update_room(room)
print_room(room)
