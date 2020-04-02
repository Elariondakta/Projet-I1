import npyscreen
import curses

class AddRoom(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, value="Mon formulaire", relx=10)

        self.add(npyscreen.TitleText, name="Batiment : ", relx=20)
        self.add(npyscreen.TitleText, name="Salle : ", relx=20, rely=5)
        self.add(npyscreen.TitleText, name="Test", relx=20)
        self.add(npyscreen.BoxTitle, name="Test", entry_widget=npyscreen.TitleText)