from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

traversal_path = []
cache = {}
rooms = {}

# Reverse directions
reverse_directions = [('n', 's'), ('s', 'n'), ('e', 'w'), ('w', 'e')]

# Reverse move through the graph
reverse_path = []

# Get the first room id and its exits stored in our cache
cache[player.current_room.id] = player.current_room.get_exits()
rooms[player.current_room.id] = player.current_room.get_exits()

# While the length of our cache dictionary is less than the length of total cache in the map
while len(cache) < len(room_graph) - 1:
    while player.current_room.id not in cache:
        room_id = player.current_room.id
        exits = player.current_room.get_exits()
        # Let's save the room_id and its exits to our cache
        cache[room_id] = exits
        rooms[room_id] = exits

        # Removing a direction from a current room indicates that we already
        # gone that path, no need to repeat later on
        reverse_direction = reverse_path[-1]
        # print(cache[room_id])
        cache[room_id].remove(reverse_direction)
        # print(cache[room_id])

    # When we reached a room with no exits, indicating that the current
    # direction we're moving is a dead end to that room, now we need to traverse
    # backward. Let's use our reverse path to figure out the way back
    while len(cache[player.current_room.id]) < 1:
        reverse_direction = reverse_path.pop()
        traversal_path.append(reverse_direction)
        player.travel(reverse_direction)

    # Randomly choose a direction for moving through the room.
    # Remove it from the current room exits, then append it to the path.
    # Removing a direction from a current room indicates that we already
    # gone that path, no need to repeat later on
    room_id = player.current_room.id
    direction = cache[room_id].pop()
    traversal_path.append(direction)

    # Keep track of a reverse path so that when the robot hits a dead end,
    # it knows how to back out
    for item in reverse_directions:
        if item[0] == direction:
            reverse_path.append(item[1])

    # Move to that direction
    player.travel(direction)

# print(rooms)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
