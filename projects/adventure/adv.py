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
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

traversal_path = []
cache = {}

# Reverse directions
reverse_directions = [('n', 's'), ('s', 'n'), ('e', 'w'), ('w', 'e')]

# List to track backwards movements through our map
reverse_path = []

# Initialize dictionaries and store current room and its exits
cache[player.current_room.id] = player.current_room.get_exits()

# While the length of our cache dictionary is less than the length of total cache in the map
while len(cache) < len(room_graph) - 1:
    # If current room is not in our cache, add it to the cache
    # with its exiting routes
    if player.current_room.id not in cache:
        cache[player.current_room.id] = player.current_room.get_exits()

        # Get the reverse of the last direction we traveled,
        # remove it from the current room since we're moving that same way
        # Indicate that we already went this direction before. Next time,
        # we'll travel the rest of the exits
        reverse_direction = reverse_path[-1]
        cache[player.current_room.id].remove(reverse_direction)
        print(player.current_room.id)

    # Randomly choose a direction for moving through the room
    # Append the direction to the path
    # Keep track of a reverse path so that when the robot hits a dead end,
    # it knows how to back out
    available_direction = cache[player.current_room.id].pop()
    traversal_path.append(available_direction)
    for item in reverse_directions:
        if item[0] == available_direction:
            reverse_path.append(item[1])
    print(available_direction)
    # reverse_path.append(inverse_directions[available_direction])
    print(player.current_room.id)

    # Move the robot to that direction
    player.travel(available_direction)

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
