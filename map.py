# This module is responsible for everything that is in the main map.
# Hash code below solves a bug in the PyCharm IDE relating to import statements.
# (Credit to https://stackoverflow.com/questions/21139329/false-unused-import-statement-in-pycharm).
# noinspection PyUnresolvedReferences
from room_generator import make_room, update_room

room = make_room(5, 5)
update_room(room)
print(room)