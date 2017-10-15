# This module currently makes and prints an empty room using simulated matrices.
# Each value in the matrix corresponds to a tile in two-dimensional space.
from player_stats import player_location


def make_room(width, height):
    # Makes a room using nested lists to simulate a matrix of values.
    room = []
    for i in range(height):
        room.append([])
    for i in range(height):
        for i in range(width):
            room[i].append("#")
    return room


def update_room(room):
    # Updates room with entity locations.
    room[player_location[1]][player_location[0]] = "@"

# Prints northern wall of room according to width. 'end' statement courtesy of
# https://stackoverflow.com/questions/5598181/python-print-on-same-line.
def print_north_wall(room):
    print("_", end="")
    for i in room[0]:
        print("____", end="")
    print("_")


# Prints the inside part of the room, along with entities if applicable.
def print_room_inside(room):
    for row in room:
        print("|", end="")
        for unit in row:
            if unit == "#":
                print("     ", end="")
            elif unit == "@":
                print("  @  ", end="")
        print("|")


def print_room(room):
    print_north_wall(room)
    print_room_inside(room)
    print_north_wall(room)

