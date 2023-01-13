import roomSetup
from inventory import inventory

print('Available items:\n [0]:Digital Recorder [1]:EMF Detector [2]:Night Vision Camera [3]:Ovilus [4]:REM-POD ['
      '5]:SLS Camera [6]:Spirit Box')
requested_item = int(input('Please enter the index of the item you would like:\n'))
requested_item2 = int(input('Please enter the index of the 2nd item you would like:\n'))

carried_items = []
current_room = roomSetup.entryway

if 0 <= requested_item < len(inventory):
    # print(inventory[requested_item])
    carried_items.append(inventory[requested_item])
else:
    print('No item found.')

if 0 <= requested_item2 < len(inventory):
    # print(inventory[requested_item2])
    carried_items.append(inventory[requested_item2])
else:
    print('No item found.')

print('You have received:')

for x in carried_items:
    print('{}'.format(x))

print(f'You are in the {current_room}')
user_action = ''

while user_action != 'end':
    user_action = input('What would you like to do?\n Possible Responses:\n use item\n move\n end\n').strip().lower()
    if user_action == 'use item':
        item_to_use = int(
            input(f'Enter an index for the item:\n [0]:{carried_items[0].name} [1]:{carried_items[1].name}\n'))
        if item_to_use <= len(carried_items):
            carried_items[item_to_use].use_item()
        else:
            print('invalid')
    if user_action == 'move':
        user_movement = input(
            'Which direction would you like to move?\n Possible Responses:\n North\n South\n East\n West\n').strip().lower()

        if user_movement == 'north' and current_room.north.lower() != 'none':
            print(f'You are in the {current_room.north}')
        elif user_movement == 'south' and current_room.south.lower() != 'none':
            print(f'You are in the {current_room.south}')
        elif user_movement == 'east' and current_room.east.lower() != 'none':
            print(f'You are in the {current_room.east}')
        elif user_movement == 'west' and current_room.west.lower() != 'none':
            print(f'You are in the {current_room.west}')
        else:
            print('Invalid direction.')
else:
    print('The end.')
