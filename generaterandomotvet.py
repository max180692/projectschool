import random


class GenerateRandomAnswer:


    def generation_random_answer(answer,sostav_chisla):
        list_variant = [random.randint(1,sostav_chisla) for i in range(6)]
        list_variant[random.randint(0,5)] = answer
        return list_variant
        