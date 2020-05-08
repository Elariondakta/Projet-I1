import npyscreen

class BreachForm(npyscreen.FormBaseNew):
    def create(self):
        self.build()

    def build(self):
        self.add(npyscreen.FixedText, name="title", value="Dernières vulnérabilitées")
                