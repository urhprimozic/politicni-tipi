import emoji #https://pypi.org/project/emoji/

class Politicni_Tip():
    """
    Razred, ki ustvari navdušenca nad politiko.
    TO DO:Ideja - razred tudi ureja besedilo, saj se bomo tako najlažje ognili boremenitvam stacka z stringi.
    """
    def __init__(self, heroj):
        self.heroj = heroj
    def daj_glas(self):
        """
        Vrne enostaven niz, s katerim povzigne svojega heroja.
        """
        return self.heroj + emoji.emojize(':purple_heart:', use_aliases=True)


#Lokalni testi
levicar = Politicni_Tip("Luka")
#velikonolčno jajse za škofijce
kristjan = Politicni_Tip("Severina")
print(levicar.daj_glas())