#!/usr/bin/env python3

def print_character_info(characters):
    for char_name, char_info in characters.items():
        for char_stat in char_info:
            value = char_info[char_stat]
            print(f"{char_name}'s {char_stat} is: {value}")

# Example usage:
marvelchars = {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    }
}

print_character_info(marvelchars)

