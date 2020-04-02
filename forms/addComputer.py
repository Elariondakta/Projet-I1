import npyscreen
import curses

class AddComputer (npyscreen.Form):
    def create(self):
        self.add (npyscreen.FixedText, value = "Specifications", relx=50)
        self.add (npyscreen.FixedText, value = "Processor : ", relx=25, rely=5)
        self.add (npyscreen.TitleText, name = "Platform : ", relx=10, rely=7)
        self.add (npyscreen.TitleText, name = "Brand : ", relx=10, rely=9)
        self.add (npyscreen.TitleText, name = "Speed : ", relx=10, rely=11)
        self.add (npyscreen.TitleText, name = "Cash Size : ", relx=10, rely=13)
        self.add (npyscreen.TitleText, name = "Model : ", relx=10, rely=15)
        self.add (npyscreen.FixedText, value = "RAM : ", relx=25, rely=18)
        self.add (npyscreen.TitleText, name = "Number : ", relx=10, rely=20)
        self.add (npyscreen.TitleText, name = "Total Size : ", relx=10, rely=22)