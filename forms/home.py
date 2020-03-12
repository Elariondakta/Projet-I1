import npyscreen
import curses
from const import *

class HomeForm(npyscreen.FormBaseNew):
    
    def create(self):
        self.build()
        
    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        
    def dispRooms(self): 
        pass
    
    def build(self):
        
        self.add(npyscreen.FixedText, name="title", value="Bienvenue sur notre gestionnaire d'ordinateur :")
        
        self.add(npyscreen.ButtonPress, name="", hidden=True)
        
        self.add(npyscreen.ButtonPress, name="> Liste des salles", when_pressed_function=lambda : self.parentApp.switchForm("ROOMS"))
        self.add(npyscreen.ButtonPress, name="> Liste des ordinateurs", when_pressed_function=lambda : self.parentApp.switchForm("COMPUTERS"))
        self.add(npyscreen.ButtonPress, name="> Liste des logiciels", when_pressed_function=lambda : self.parentApp.switchForm("SOFTWARES"))
        self.add(npyscreen.ButtonPress, name="> Vulnérabilitées", when_pressed_function=lambda : self.parentApp.switchForm("BREACH"))
        self.add(npyscreen.ButtonPress, name="", hidden=True)
        self.add(npyscreen.ButtonPress, name="> Besoin d'aide ?", when_pressed_function=lambda : self.parentApp.switchForm(None))
        self.add(npyscreen.ButtonPress, name="", hidden=True)
        self.add(npyscreen.ButtonPress, name="", hidden=True)
        self.add(npyscreen.ButtonPress, name="> Quitter", when_pressed_function=lambda : self.parentApp.switchForm(None))
        
        