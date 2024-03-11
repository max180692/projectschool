
class DelenieAndUmnojenie:

    def __init__(self):
        self.count_sostav_chisla = 0
        #self.list_random_primer = []

    def set_sostav_chisla(self,sostav_chisla):
        self.count_sostav_chisla = sostav_chisla
    

    def create_primer(self):
        #print(self.count_sostav_chisla)
        #self.list_random_primer = []
        for i in range(1,11):
            #\u00D7 знак умножения
            if self.action == '\u00D7':
                self.primer = f'{self.count_sostav_chisla} \u00D7 {i}'
                self.list_random_primer.append(self.primer)
            #\u00F7 знак деления
            elif self.action == '\u00F7':
                if i % self.count_sostav_chisla == 0 :
                    self.primer = f'{i} \u00F7 {self.count_sostav_chisla}'
                    self.list_random_primer.append(self.primer)
                if i*self.count_sostav_chisla % self.count_sostav_chisla == 0:
                    self.primer = f'{i*self.count_sostav_chisla} \u00F7 {self.count_sostav_chisla}'
                    self.list_random_primer.append(self.primer)

    def generation_primer(self,action,random_primer=False):
        self.list_random_primer = []
        #Задание переменной какого-то числа
        #Генерация примеров
        self.action = action
        
        if len(self.list_random_primer)>0 and not random_primer :
            self.list_random_primer.clear()
        #if len(self.list_random_primer)>0 and  random_primer :
        #    self.list_random_primer.clear()
        self.create_primer()

    def get_list_primer(self):
        return self.list_random_primer
        

    
#print(list_random_index)

