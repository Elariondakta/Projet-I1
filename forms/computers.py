import npyscreen

class ComputersForm(npyscreen.FormBaseNew):
    def create(self):
        self.build()

    def build(self):
        self.add(npyscreen.FixedText, name="title", value="Ordinateurs : ")