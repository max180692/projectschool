

class SlojenieAndVichitanieChisel:

    def __init__(self):
        self.count_sostav_chisla = 0
        self.list_random_primer = []

    def set_sostav_chisla(self,sostav_chisla):
        self.count_sostav_chisla = sostav_chisla

    def create_primer(self):
        #print(self.count_sostav_chisla)
        for i in range(self.count_sostav_chisla):
            if self.action == '+':
                self.primer = f'{self.count_sostav_chisla-i} + {i}'
            elif self.action == '-':
                self.primer = f'{self.count_sostav_chisla} - {i}'
            self.list_random_primer.append(self.primer)

    def generation_primer_slojenie(self,action):
        #Задание переменной какого-то числа
        #Генерация примеров
        self.action = action
        if len(self.list_random_primer)>0:
            self.list_random_primer.clear()
        while self.count_sostav_chisla > 0:
            self.create_primer()
            self.count_sostav_chisla -= 1

    def get_list_primer(self):
        return self.list_random_primer
        

    
#print(list_random_index)

