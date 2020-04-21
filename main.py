import npyscreen
from app import App
from api import API
# Redirect stdout and stderr to files
import sys

if __name__ == '__main__':
    API.loadData()  #On charge la base de donnée
    App = App() #On instancie la classe App   
    App.run()   #Et on la lance