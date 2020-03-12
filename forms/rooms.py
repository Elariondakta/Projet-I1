import npyscreen

class RoomsForm(npyscreen.FormBaseNew):
    def create(self):
        self.build()

    def build(self):
        self.add(npyscreen.FixedText, name="title", value="Salles : ")
        