marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")

char_stat = input("what statistic do you want to know about? (real name, powers, archenemy)")

print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

# Display the list of characters to choose from
#print("Choose a character:")
#for index, char_name in enumerate(marvelchars.keys(), start=1):
#    print(f"{index}. {char_name}")

# Ask the user to choose a character
#choice = int(input("Pick a number for your character: "))
#char_name = list(marvelchars.keys())[choice - 1]
# Print information for the chosen character
#char_info = marvelchars[char_name]
#for char_stat, value in char_info.items():
#    print(f'The "{char_name}"\'s {char_stat} is: {value}')
