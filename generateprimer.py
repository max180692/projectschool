from generaterandomindex import GenerateRandomIndex
from slojenieandvichitaniechisel import SlojenieAndVichitanieChisel
from generaterandomotvet import GenerateRandomAnswer
from delenieandumnojenie import DelenieAndUmnojenie
from mystikers import MyStikers
import settings

class GeneratePrimer:
    # установка всех нужных классов для работы бота
    def __init__(self):
        self.sostav_chisla = 0
        self.slojenieandvichitaniechisel = SlojenieAndVichitanieChisel()
        self.delenieandumnojenie = DelenieAndUmnojenie()
        self.generate_otvet = GenerateRandomAnswer
        self.generaterandomindex = GenerateRandomIndex
        self.get_stikers = MyStikers
        self.answer = 0
        self.count = 0
        self.message_my_count = ''

    #управление установкой числа для настройки бота
    def set_sostav_chisla(self,sostav_chisla):
        self.sostav_chisla = sostav_chisla
        
    #создание списка случайных примеров на + и -
    def create_multiple_primerov(self,counts):
        self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
        self.slojenieandvichitaniechisel.generation_primer(settings.tuple_action_slojen_vichitan[0],True)
        self.list_primer = self.slojenieandvichitaniechisel.get_list_primer()
        self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
        self.slojenieandvichitaniechisel.generation_primer(settings.tuple_action_slojen_vichitan[1],True)
        self.list_primer = self.list_primer + self.slojenieandvichitaniechisel.get_list_primer()
        self.counts_primer = counts
    
    # создание случайных индексов для выбора примеров
    def create_random_multiple_index(self):
        self.list_random_index1 = self.generaterandomindex.generation_random_index(self.list_primer)



    #создание нового списка примеров где все примеры расставлены случайным образом
    def create_new_random_primer(self):
        self.list_random= []
        for i in range(self.counts_primer):
            self.list_random.append(self.list_primer[self.list_random_index1.pop(0)])
        if len(self.list_random)>0:
            self.list_random_index1.clear()



    #выбор конкретного действия для создания примеров
    def enter_action(self,action):
        self.my_action = action
        if action in settings.tuple_action_slojen_vichitan:
            self.slojenieandvichitaniechisel.set_sostav_chisla(self.sostav_chisla)
            self.slojenieandvichitaniechisel.generation_primer(settings.tuple_action_slojen_vichitan[settings.tuple_action_slojen_vichitan.index(action)])
            self.list_primer = self.slojenieandvichitaniechisel.get_list_primer()
            self.counts_primer = len(self.list_primer)
        if action in settings.tuple_action_umnoj_delenie:
            self.delenieandumnojenie.set_sostav_chisla(self.sostav_chisla)
            self.delenieandumnojenie.generation_primer(settings.tuple_action_umnoj_delenie[settings.tuple_action_umnoj_delenie.index(action)])
            self.list_primer = self.delenieandumnojenie.get_list_primer()
            self.counts_primer = len(self.list_primer)
    
    
    #получение случайных индексов в зависимости от длины списка примеров
    def get_random_index(self):
        self.list_random = self.generaterandomindex.generation_random_index(self.list_primer)
        #print(self.list_random,'this function random')

#доработать логику работы выпада примеров
#
#

    #получение случайного примера из списка
    def get_random_primer(self):
        #print(type(self.list_random[0]))
        if self.list_random:
            if len(self.list_random) > 0:
                if self.list_random[0].__class__.__name__ == 'str':
                    self.primer = self.list_random.pop()
                    #index = self.list_random.pop()  
                    #self.primer = self.list_primer[index]
                    return self.primer
                if self.list_random[0].__class__.__name__ == 'int':
                    index = self.list_random.pop()  
                    self.primer = self.list_primer[index]
                    return self.primer
        return {'message':"Примеры закончились! Ура!\nВсего примеров было "+str(self.counts_primer)+'\n' + 'Правильных ответов ' + str(self.count) + '\n'+ 'Неправильных ответов ' + str(self.counts_primer - self.count),'stiker':self.get_stikers.get_stkers_best_count()}
            
    #отпарвка в бота примера, а так же сохранение ответа
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
        
        elif '\u00D7' in self.primer:
            num1 , num2 = self.primer.split('\u00D7')
            self.answer = int(num1) * int(num2)
            self.dict_answer_primer = {'answer':self.answer}
            self.dict_answer_primer['variants_answers'] = self.generate_otvet.generation_random_answer(self.answer,self.answer+self.sostav_chisla)
            return self.dict_answer_primer

        elif '\u00F7' in self.primer:
            num1 , num2 = self.primer.split('\u00F7')
            self.answer = int(num1) // int(num2)
            self.dict_answer_primer = {'answer':self.answer}
            self.dict_answer_primer['variants_answers'] = self.generate_otvet.generation_random_answer(self.answer,self.answer + self.sostav_chisla)
            return self.dict_answer_primer
        
        return "Примеры закончились"
    
    #проверка ответа введенного в боте
    def answers(self,my_answer):
        if int(my_answer) == self.dict_answer_primer['answer']:
            self.count += 1
            if self.count in settings.tuple_true_answer:
                return {'message':'Ура! У тебя ' + str(self.count) +'  правильных ответов '  ,'stiker':self.get_stikers.get_stkers_best_count()}
        
            return {'message':'Ответ правильный!' +'\nКол-во правильных ответов ' + str(self.count),'stiker':self.get_stikers.get_stikers_answer_true()}
        
        return {'message':'Ответ неправильный! Правильный ответ ' + str(self.dict_answer_primer['answer']),'stiker':self.get_stikers.get_stikers_answer_false()}
    
    #очистка очков
    def clear_count(self):
        self.count=0




