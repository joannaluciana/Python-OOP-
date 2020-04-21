filter_maska = ["tlen", "virusy", "grzyby", "pleśń" ]


filtered_gems = filter (lambda x :  x!="tlen", filter_maska)
print(list(filtered_gems))

herbatka = ["fusy", "woda", "cukier", "esencja"]

filtr_fusik = filter (lambda x : x!='fusy', herbatka)
print (list(filtr_fusik))