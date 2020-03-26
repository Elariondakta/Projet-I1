import npyscreen
from app import App

# Redirect stdout and stderr to files
import sys

if __name__ == '__main__':
    
    App = App() #On instancie la classe App   
    App.run()   #Et on la lance