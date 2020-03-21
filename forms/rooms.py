import npyscreen

   
class SearchTextField(npyscreen.Textfield):
    def __init__(self, *args, **keywords):
        super(SearchTextField, self).__init__(*args, **keywords)
        self.editable = True
  
class SearchBar(npyscreen.BoxTitle):
    _contained_widget = SearchTextField
        
class RoomsResults(npyscreen.BoxTitle):
    _contained_widget = 
class RoomsForm(npyscreen.Form):
    def create(self):
        self.build()

    def build(self):
        self.add(SearchBar, name="Rechercher une salle : ", 
            max_height=4,
            max_width=50,
            relx=30,
            rely=1,
        )
        self.add(npyscreen.FixedText, name="title", value="Salles : ")
