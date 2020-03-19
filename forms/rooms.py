import npyscreen

class RoomsForm(npyscreen.Form):
    def create(self):
        self.build()

    def build(self):
        self.add(npyscreen.FixedText, name="title", value="Salles : ")
        