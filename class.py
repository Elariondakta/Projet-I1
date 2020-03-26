
class Vehicule:
    def __init__(self, couleur_input, marque_input):
        self.couleur = couleur_input
        self.marque = marque_input
        self.rouler()
        pass

    def rouler(self):
        pass

    def reculer(self):
        pass

# self : renvoie à la classe en elle même
# super : renvoie renvoie classe mère
class Voiture(Vehicule):
    


    def __init__(self, couleur_input, marque_input):
        super().__init__(couleur_input, marque_input)

    @staticmethod
    def rouler_toutes_les_voitures():
        pass


audi_noire = Voiture("noire", "audi")   #Audi noire est 

audi_noire.rouler()

punto_rouge = Voiture("rouge", "Fiat")

punto_rouge.rouler()

#J'appelle cette fonction sans instancier Voiture
Voiture.rouler_toutes_les_voitures()