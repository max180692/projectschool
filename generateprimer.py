from generaterandomindex import GenerateRandomIndex
from slojenieandvichitaniechisel import SlojenieAndVichitanieChisel
from generaterandomotvet import GenerateRandomAnswer
from mystikers import MyStikers
import settings

class GeneratePrimer:

    def __init__(self):
        self.sostav_chisla = 0
        self.slojenieandvichitaniechisel = SlojenieAndVichitanieChisel()
        self.generate_otvet = GenerateRandomAnswer
        self.generaterandomindex = GenerateRandomIndex
        self.get_stikers = MyStikers
        self.answer = 0
        self.count = 0
        self.message_my_count = ''

    def set_sostav_chisla(self,sostav_chisla):
        self.sostav_chisla = sostav_chisla
        

    def create_multiple_primerov(self,counts):
        self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
        self.slojenieandvichitaniechisel.generation_primer(settings.tuple_action[0],True)
        self.list_primer = self.slojenieandvichitaniechisel.get_list_primer()
        
        self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
        self.slojenieandvichitaniechisel.generation_primer(settings.tuple_action[1],True)
        self.list_primer = self.list_primer + self.slojenieandvichitaniechisel.get_list_primer()
        self.counts_primer = counts
        
    def create_random_multiple_index(self):
        self.list_random_index1 = self.generaterandomindex.generation_random_index(self.list_primer)
        
    def create_new_random_primer(self):
        self.list_random= []
        for i in range(self.counts_primer):
            self.list_random.append(self.list_primer[self.list_random_index1.pop(0)])

        if len(self.list_random)>0:
            self.list_random_index1.clear()
            

    def enter_action(self,action):
        self.my_action = action
        if action in settings.tuple_action:
            self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
            self.slojenieandvichitaniechisel.generation_primer(settings.tuple_action[settings.tuple_action.index(action)])
            self.list_primer = self.slojenieandvichitaniechisel.get_list_primer()
            self.counts_primer = len(self.list_primer)
    
    

    def get_random_index(self):
        self.list_random = self.generaterandomindex.generation_random_index(self.list_primer)



#
#


    def get_random_primer(self):
        #print(type(self.list_random[0]))
        if self.list_random:
            if len(self.list_random) > 0:
                if self.list_random[0].__class__.__name__ == 'str':
                    #print(self.list_random)
                    self.primer = self.list_random.pop()
                    #index = self.list_random.pop()  
                    #self.primer = self.list_primer[index]
                    return self.primer
                if self.list_random[0].__class__.__name__ == 'int':
                    #print(len(self.list_random),'/////')
                    index = self.list_random.pop()  
                    self.primer = self.list_primer[index]
                    return self.primer
        return {'message':"Примеры закончились! Ура!\nВсего примеров было "+str(self.counts_primer)+'\n' + 'Правильных ответов ' + str(self.count) + '\n'+ 'Неправильных ответов ' + str(self.counts_primer - self.count),'stiker':self.get_stikers.get_stkers_best_count()}
            
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
            if self.count in settings.tuple_true_answer:
                return {'message':'Ура! У тебя ' + str(self.count) +'  правильных ответов '  ,'stiker':self.get_stikers.get_stkers_best_count()}
        
            return {'message':'Ответ правильный!' +'\nКол-во правильных ответов ' + str(self.count),'stiker':self.get_stikers.get_stikers_answer_true()}
        
        return {'message':'Ответ неправильный! Правильный ответ ' + str(self.dict_answer_primer['answer']),'stiker':self.get_stikers.get_stikers_answer_false()}
    
    def clear_count(self):
        self.count=0
