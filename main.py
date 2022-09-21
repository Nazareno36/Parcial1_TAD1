'''
    Author: Carlos Andrés Páez
    Date: 21/09/2022
    version: 1.0
'''

from solucion import Solution

solution = Solution()
#Punto1.
solution.add_serie()

print(solution.series)
print("\n\n")

#Punto2.
# solution.series = [{'serie': 'cocoman', 'number_seasons': 2, 'original_lenguage': 'esp', 'features_seasons': [{'season_number': 1, 'season_name': 'a', 'premier_date': '1', 'cast': ['carlos', 'roberto'], 'episodes': [{'episode_name': 'je', 'time_duration': 2}, {'episode_name': 'je', 'time_duration': 2}]}, {'season_number': 2, 'season_name': 'jesus te ama', 'premier_date': '13', 'cast': ['Carlos'], 'episodes': [{'episode_name': 'a', 'time_duration': 2}]}]}, {'serie': 'joselito', 'number_seasons': 2, 'original_lenguage': 'eng', 'features_seasons': [{'season_number': 1, 'season_name': 'jesus nos ama a todos', 'premier_date': '16', 'cast': ['carlos', 'roberto'], 'episodes': [{'episode_name': 'b', 'time_duration': 5}, {'episode_name': 'b', 'time_duration': 5}]}, {'season_number': 2, 'season_name': 'a', 'premier_date': '4', 'cast': ['roberto', 'carlos'], 'episodes': [{'episode_name': 'ca', 'time_duration': 4}, {'episode_name': 'ca', 'time_duration': 4}]}]}, {'serie': 'carlitos super estrella', 'number_seasons': 2, 'original_lenguage': 'esp', 'features_seasons': [{'season_number': 1, 'season_name': 'a', 'premier_date': '2', 'cast': ['Carlos'], 'episodes': [{'episode_name': 'asdasd', 'time_duration': 1}]}, {'season_number': 2, 'season_name': 'casd', 'premier_date': '123', 'cast': ['sindy'], 'episodes': [{'episode_name': 'cjaksjfialsd', 'time_duration': 123124124}]}]}]
#A.
solution.series_by_actor(input("buscar series por actor --> "))
print("\n\n")

#B.
solution.series_in_lenguage(input("buscar series por lenguaje --> "))
print("\n\n")

#C.
solution.delete_series_on_premier_date(input("Eliminar series con fecha de estreno --> "))
print(solution.series)
