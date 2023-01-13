import random


class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def use_item(self):
        pass


class DigitalRecorder(Item):

    def __init__(self, name):
        super().__init__(name)

    def use_item(self):
        responses = ['...Get out!...', 'Help', '...Kitchen...', 'Se..cret..', 'Where are they?']
        print(f"Digital Recorder Feedback: {responses[random.randint(0, len(responses)-1)]}")


class Ovilus(Item):
    def __init__(self, name):
        super().__init__(name)

    def use_item(self):
        word_library = ['Demon', 'Kill', 'Buried', 'Altar']
        print(f"Ovilus Feedback: {word_library[random.randint(0, len(word_library)-1)]}")


class SLScamera(Item):
    def __init__(self, name):
        super().__init__(name)

    def use_item(self):
        print(" /")
        print("\\___")
        print("  |")
