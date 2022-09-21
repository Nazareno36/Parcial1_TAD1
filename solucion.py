
class Solution:

    def __init__(self) :
        self.series = []
    
    #punto 1:

    def addSerie(self):
        while True:
            try:
                series = int(input("Ingrese la cantidad de series --> "))
                break
            except:
                print("Entrada no valida")
    
        for i in range (1, series+1):
            serie = {
                "serie" : "",
                "number_seasons" : 0,
                "original_lenguage" : "",
                "features_seasons": []
            }
            serie["serie"] = input("Llene la siguiente informacion\nnombre de la serie --> ")
            while True:
                try:
                    serie["number_seasons"] = int(input("numero de temporadas --> "))
                    break
                except:
                    print("Entrada no valida")
            serie["original_lenguage"] = input("Lenguaje original --> ")
            seasons = serie["number_seasons"]
            for i in range(1,seasons+1):
                serie["features_seasons"].append(self.addSeason())
            self.series.append(serie)


    def addSeason(self):
        season = {
            "season_number" : 0,
            "season_name": "",
            "premier_date": "",
            "cast": [],
            "episodes": []
        }
        while True:
            try:
                season["season_number"] = int(input("Llene la siguiente informacion sobre las temporadas\ntemporada numero --> "))
                break
            except:
                print("Entrada no valida")
        season["season_name"] = input("nombre de temporada --> ")
        season["premier_date"] = input("Fecha de estreno --> ")
        while True:
            try:
                actors = int(input("Ingrese la cantidad de actores --> "))
                break
            except:
                print("Entrada no valida")
        for i in range(1,actors+1):
            season["cast"].append(input(f"Nombre del actor numero {i} --> "))
        while True:
            try:
                episodes = int(input("Ingrese la cantidad de episodios --> "))
                break
            except:
                print("Entrada no valida")
        episode = {
            "episode_name": "",
            "time_duration": 0,
        }
        for i in range(1,episodes+1):
            episode["episode_name"] = input(f"Nombre del episodio numero {i} --> ")
            while True:
                try:
                    episode["time_duration"] = int(input(f"Duracion del episodio numero {i} --> "))
                    break
                except:
                    print("Entrada no valida") 
            season["episodes"].append(episode)
        
        return season

    