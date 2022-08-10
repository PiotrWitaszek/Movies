class Movies:
    def __init__(self, title, year, kind, views):
        self.title = title
        self.year = year
        self.kind = kind
        self.views = views

    def play(self):
        self.views = int(self.views) + 1
  
    def __repr__(self):
        return f'{self.title} {self.year}'
          
class Series(Movies):
        def __init__(self, season, episode, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.season = season
            self.episode = episode        
        def __str__(self):
          return f"{self.title} S{int(self.season):02d}E{int(self.episode):02d}"

def search(list, value):
  for i in range(0, len(list)):
    if list[i] == value:
      print(value)
  return False

def get_series():
  for i in range(0, len(list)):
    if isinstance(list[i], Series):
      series_list.append(list[i])

def get_movies():
  for i in range(0, len(list)):
    if isinstance(list[i], Series) == False:
       movies_list.append(list[i])
      
  
if __name__ == '__main__':
    list = [] 
    series_list = []
    movies_list = []
    Shawshank = Movies("Shawshank redemption", "1994", "Drama", "22")
    list.append(Shawshank)
    Godfather = Movies("The Godfather", "1972", "Drama", "24")
    list.append(Godfather)
    Psycho = Movies("Psycho", "1960", "Thriller", "19")
    list.append(Psycho)
    Requiem = Movies("Requiem for a dream", "2000", "Drama", "14")
    list.append(Requiem) 
    Peaky = Series("1", "4", "Peaky Blinders", "2013", "Drama", "22")
    list.append(Peaky)
    Bad = Series("3", "9", "Breaking Bad", "2008", "Drama", "7")
    list.append(Bad)
#wszystko poniżej celem sprawdzenia kodu - wrzucać to też w  maine?
get_movies()
search(list, Bad)
get_series()
print(series_list)
print(movies_list)

print(Godfather)
print(Peaky)
Peaky.play()
print(Peaky.views)
print(list)
