import npyscreen
import curses
#hiskfsdzzdzz
#ssjdsjdsdsj
#"software": {
#            "name": "OpenOffice",
#            "editor": "Francis",
#            "provider": "Microsoft",
#            "version": "2.4.3892",
#            "licence_exp_date": 3456787456,
#            "ID": "trhdfg3356",
#            "add_on": {
#                "ID": "trhdfg3356",
#                "name": "OpenOffice",
#                "editor": "Francis",
#                "provider": "Microsoft",
#                "version": "2.4.3892"


class addSoftware(npyscreen.Form):      
    def create(self):  
        self.add(npyscreen.TitleText, value="Titre", relx=10)
        self.add(npyscreen.TitleText,  value="Champ", relx=10)
        self.add(npyscreen.ComboBox, value= " coucou", display_value="text") 
