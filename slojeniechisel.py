

class SlojenieChisel:

    def generation_primer_slojenie(self):
        #Задание переменной какого-то числа
        #Генерация примеров
        list_random_primer = []
        for i in range(self.sostav_chisla):
            primer = f'{self.sostav_chisla-i} + {i}'
            list_random_primer.append(primer)
        return list_random_primer

    
#print(list_random_index)

