from libstikers import LIBSTIKERS
import random

class MyStikers:

    def get_stikers_answer_true():
        random_index = random.randint(0,len(LIBSTIKERS['answer_true'])-1)
        return LIBSTIKERS['answer_true'][random_index]
    
    def get_stikers_answer_false():
        random_index = random.randint(0,len(LIBSTIKERS['answer_false'])-1)
        return LIBSTIKERS['answer_false'][random_index]
    
    def get_stkers_best_count():
        random_index = random.randint(0,len(LIBSTIKERS['best_score'])-1)
        return LIBSTIKERS['best_score'][random_index]