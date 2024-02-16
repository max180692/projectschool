from generaterandomindex import GenerateRandomIndex
from slojenieandvichitaniechisel import SlojenieAndVichitanieChisel
from generaterandomotvet import GenerateRandomAnswer

class GeneratePrimer:

    def __init__(self):
        self.sostav_chisla = 0
        self.slojenieandvichitaniechisel = SlojenieAndVichitanieChisel()
        self.generate_otvet = GenerateRandomAnswer
        self.generaterandomindex = GenerateRandomIndex
        self.answer = 0
        self.count = 0

    def set_sostav_chisla(self,sostav_chisla):
        self.sostav_chisla = sostav_chisla
        


    def enter_action(self,action):
        if action == '+':
            self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
            self.slojenieandvichitaniechisel.generation_primer(action)
            self.list_primer = self.slojenieandvichitaniechisel.get_list_primer()
            self.counts_primer = len(self.list_primer)
        elif action == '-':
            self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
            self.slojenieandvichitaniechisel.generation_primer(action)
            self.list_primer = self.slojenieandvichitaniechisel.get_list_primer()
            self.counts_primer = len(self.list_primer)
            
        
    def get_random_index(self):
        self.list_random = self.generaterandomindex.generation_random_index(self)

    def get_random_primer(self):
        if len(self.list_random) > 0:
            index = self.list_random.pop()  
            self.primer = self.list_primer[index]
            return self.primer
        return "Примеры закончились! Ура! Всего было "+str(self.counts_primer)+'\n' + 'Правильных ответов ' + str(self.count)
            
    def get_answer(self):
        if '+' in self.primer:
            num1 , num2 = self.primer.split('+')
            self.answer = int(num1) + int(num2)
            self.dict_answer_primer = {'answer':self.answer}
            self.dict_answer_primer['variants_answers'] = self.generate_otvet.generation_random_answer(self.answer,self.sostav_chisla)
            return self.dict_answer_primer
        
        elif '-' in self.primer:
            num1 , num2 = self.primer.split('-')
            self.answer = int(num1) - int(num2)
            self.dict_answer_primer = {'answer':self.answer}
            self.dict_answer_primer['variants_answers'] = self.generate_otvet.generation_random_answer(self.answer,self.sostav_chisla)
            return self.dict_answer_primer
        return "Примеры закончились"
    
    def answers(self,my_answer):
        if int(my_answer) == self.dict_answer_primer['answer']:
            self.count += 1
            return 'Ответ правильный! ' + str(self.dict_answer_primer['answer']) + 'Кол-во правильных ответов ' + str(self.count)
        return 'Ответ неправильный! Правильный ответ ' + str(self.dict_answer_primer['answer']) 