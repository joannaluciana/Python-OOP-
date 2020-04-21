class Cat:
    def __init__(self, imie, rasa, waga, sluga):
        self.imie = imie
        self.rasa = rasa
        self.waga = waga
        self.sluga = sluga

    def __str__(self):
        return f"""Jestem {self.imie} kot waze {self.waga} kg
moim sluga jest {self.sluga} jestem rasowcem rasy {self.rasa} """

    def glaskanie(self, cat_bod):
        if cat_bod == "head":
            print("mrrrrr good good")
        elif cat_bod == "tail":
            print('mrrrrrr miaux better better')
        else:
            print('You stupid human creature - do not touch this area!!!')

    def feeding(self, cat_food, food_weight):
        if self.rasa == "dachowiec":
            print('Pls give tuna and pork')
        elif self.rasa == "syjam":
            print('pls give me caviar and diamonds')

        if cat_food==True:
            self.waga += food_weight
            print("Cat weight is" )
            print(self.waga)
        else:
            print('I am starving  :(')


cat1 = Cat('Moris', 'dachowiec', 3, 'Joanna Wloskowicz')
print(cat1)
cat1.cat_bod = input('Stroke me servant!!!!: type head or tail ')
cat1.glaskanie(cat1.cat_bod)

k = input('Feed me - Pls type Y/N')
if k == "Y":
    cat1.feeding(True, 300)
else:
    cat1.feeding(False, 0)