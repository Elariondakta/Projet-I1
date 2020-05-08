import npyscreen
import curses

class AddUSB (npyscreen.ActionFormV2):
    def create (self):
        self.add (npyscreen.FixedText, value = "USB :", relx=25)
        self.nextrely += 1
        self.add (npyscreen.TitleText, name = "Type :", relx=10)
        self.add (npyscreen.TitleText, name = "Port n° :", relx=10)
        self.add (npyscreen.TitleText, name = "Size :", relx=10)