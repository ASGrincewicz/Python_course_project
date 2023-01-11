# List of items that must be collected to finish game.
from item import Item, Ovilus, SLScamera

# Items: Ovilus, Digital Recorder, SLS Camera, Spirit-Box, Night Vision Camera, EMF Detector, REM-POD

# inventory = ['Digital Recorder', 'EMF Detector', 'Night Vision Camera', 'Ovilus', 'REM-POD', 'SLS Camera',
# 'Spirit-Box']


digital_recorder = Item('Digital Recorder')
emf_detector = Item('EMF Detector')
night_vision = Item('Night Vision Camera')
ovilus = Ovilus('Ovilus')
rem_pod = Item('REM-POD')
sls_camera = SLScamera('SLS Camera')
spirit_box = Item('Spirit Box')

inventory = [digital_recorder, emf_detector, night_vision, ovilus, rem_pod, sls_camera, spirit_box]


def use_item(index):
    inventory[index].use_item()
