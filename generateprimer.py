from generaterandomindex import GenerateRandomIndex
from slojeniechisel import SlojenieChisel
from vichitaniechisel import VichitanieChisel

class GeneratePrimer:

    def __init__(self,sostav_chisla):
        self.sostav_chisla = sostav_chisla
        self.slojeniechisel = SlojenieChisel
        self.vichitaniechisel = VichitanieChisel
        self.generaterandomindex = GenerateRandomIndex

    def enter_action(self,action):
        if action == '+':
            return self.slojeniechisel.generation_primer_slojenie(self)
        elif action == '-':
            return self.vichitaniechisel.generation_primer_vichitanie(self)
        
    def get_random_index(self):
        return self.generaterandomindex.generation_random_index(self)
            