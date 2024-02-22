import random


class GenerateRandomIndex:
    
     def generation_random_index(list_element):
            #генерация рандомных индексов
        list_random_index = []
        random_index = random.randint(0,len(list_element)-1)
        while len(list_random_index) != len(list_element):
            if random_index in list_random_index:
                random_index = random.randint(0,len(list_element)-1)
            else:
                list_random_index.append(random_index)
        return list_random_index