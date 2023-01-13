# Scenario: Text-based Metroid-vania style layout with Paranormal investigation theme.
# Rooms: Entryway, Kitchen, Master Bedroom, Closet, Dining Room, Living Room, Office, Stairway, Altar Room

from room import Room

floor_plan = ['none', 'Entryway', 'Kitchen', 'Master Bedroom', 'Closet', 'Dining Room', 'Office', 'Stairway',
              'Living Room', 'Altar']

# Need to map out floor plan
entryway = Room("Entryway", floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])
kitchen = Room('Kitchen', floor_plan[3], floor_plan[0], floor_plan[4], floor_plan[5])
master_bedroom = Room('Master Bedroom', floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])
closet = Room('Closet', floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])
dining_room = Room('Dining Room', floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])
office = Room('Office', floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])
stairway = Room('Stairway',floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])
living_room = Room('Living Room', floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])
altar = Room('Altar', floor_plan[2], floor_plan[0], floor_plan[4], floor_plan[5])


def get_room(room) -> str:
    match room:
        case 'entryway':
            return entryway
        case 'kitchen':
            return kitchen
        case 'master bedroom':
            return master_bedroom
        case 'closet':
            return closet
        case 'dining room':
            return dining_room
        case 'office':
            return office
        case 'stairway':
            return stairway
        case 'living room':
            return living_room
        case 'altar':
            return altar
