import npyscreen

class SoftwareForm(npyscreen.FormMultiPageAction):
    def create(self):
        self.build()

    def build(self):
        self.add(npyscreen.FixedText, name="title", value="Logiciels : ")