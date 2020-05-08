import npyscreen
import curses

class ButtonAddUSB(npyscreen.ButtonPress):
    def __init__(self, *args, **keywords):
        super(ButtonAddUSB, self).__init__(*args, **keywords)
        self.name="Ajouter_un_Port_USB"
        
    def whenPressed(self):
        self.find_parent_app().switchForm("ADD_USB")

class ButtonAddUSBBox(npyscreen.BoxTitle):
    _contained_widget = ButtonAddUSB

class AddComputer(npyscreen.FormMultiPageAction):
    def create(self):
        self.build()
    
    def build(self):
        self.add_widget_intelligent (npyscreen.FixedText, value = "Specifications", relx=50)
        self.add_widget_intelligent (npyscreen.FixedText, value = "Processor : ", relx=25, rely=4)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Platform : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Brand : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Speed : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Cash Size : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Model : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "RAM : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Number : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Total Size : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "Graphic Card : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Brand : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Memory : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Model : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "Video Port : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "VGA : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "HDMI : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "Screen : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Resolution : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Size X : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Size Y : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "Network Card : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Speed : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Brand : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "Localisation : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Building : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Room : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "User : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Name : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Username : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "ID : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "Purchase : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.TitleText, name = "Maker : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleText, name = "Provider : ", relx=10)
        self.add_widget_intelligent (npyscreen.TitleDateCombo, name = "Purchase Date Timestamp : ", relx=10, allowClear=False)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.FixedText, value = "Further Features : ", relx=25)
        self.nextrely += 1
        self.add_widget_intelligent (npyscreen.RoundCheckBox, name = "CD Player : ", relx=10)
        self.add_widget_intelligent (npyscreen.RoundCheckBox, name = "WIFI : ", relx=10)
        self.add_widget_intelligent (npyscreen.RoundCheckBox, name = "Bluetooth : ", relx=10)
        self.nextrely += 1
        self.add_widget_intelligent (ButtonAddUSB)


def on_ok(self):
        self.find_parent_app().switchForm("COMPUTERS")

def on_cancel(self):
        self.find_parent_app().switchForm("COMPUTERS")