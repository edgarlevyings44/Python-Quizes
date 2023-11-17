class ChipComponent:
    def __init__(self, max_chips, max_text_length):
        self.max_chips = max_chips
        self.max_text_length = max_text_length
        self.chips = []

    def add_chip(self, text):
        if len(self.chips) < self.max_chips and len(text) <= self.max_text_length:
            self.chips.append(text)
            return True
        return False

    def display_chips(self):
        for chip in self.chips:
            print(chip)

# Sample usage:
component = ChipComponent(max_chips=3, max_text_length=6)

sampleChips = [
    { 'label': "123456" },
    { 'label': "1234567" },
    { 'label': "12345678" },
    { 'label': "12345" },
    { 'label': "123456789" }
]

for chip in sampleChips:
    component.add_chip(chip['label'])

# Displaying the chips
result = component.display_chips(component.chips, maxChipsDisplayed=3, maxTextLength=6)
for item in result:
    print(item)