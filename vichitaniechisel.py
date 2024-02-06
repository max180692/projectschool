
class VichitanieChisel:

    def generation_primer_vichitanie(self):
        list_random_primer = []
        for i in range(self.sostav_chisla):
            primer = f'{self.sostav_chisla} - {i}'
            list_random_primer.append(primer)
        return list_random_primer