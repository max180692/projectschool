import random


class GenerateRandomIndex:
    
    def generation_random_index(self):
            #генерация рандомных индексов
        list_random_index = []
        random_index = random.randint(0,len(self.list_primer)-1)
        while len(list_random_index) != len(self.list_primer):
            if random_index in list_random_index:
                random_index = random.randint(0,len(self.list_primer)-1)
            else:
                list_random_index.append(random_index)
        return list_random_index