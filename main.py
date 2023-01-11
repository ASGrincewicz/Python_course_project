import roomSetup
from inventory import inventory

requested_item = int(input('Please enter the index of the item you would like:\n'))
requested_item2 = int(input('Please enter the index of the 2nd item you would like:\n'))

carried_items = []

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
