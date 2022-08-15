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
        def __repr__(self):
          return f"{self.title} S{int(self.season):02d}E{int(self.episode):02d}"

def search(list, value):
  for elem in list:
    if elem == value:
      return print(value)
  return False
  #tego za cholerę nie mogę ogarnąć, wpadłem na takie coś:
#if "Psycho" in [data.title for data in list]:
  #print(nie wiem co wpisac by printowało object)
      
def get_series():
  for elem in list:
    if type(elem) is (Series):
      series_list.append(elem)
  return series_list

def get_movies():
  for elem in list:
    if type(elem) is (Movies):
       movies_list.append(elem)
  return movies_list
  
  
if __name__ == '__main__':
  list = [] 
  series_list = []
  movies_list = []
  Shawshank = Movies("Shawshank_redemption", "1994", "Drama", "22")
  list.append(Shawshank)
  Godfather = Movies("The_Godfather", "1972", "Drama", "24")
  list.append(Godfather)
  Psycho = Movies("Psycho", "1960", "Thriller", "19")
  list.append(Psycho)
  Requiem = Movies("Requiem_for_a_dream", "2000", "Drama", "14")
  list.append(Requiem) 
  Peaky = Series("1", "4", "Peaky_Blinders", "2013", "Drama", "22")
  list.append(Peaky)
  Bad = Series("3", "9", "Breaking_Bad", "2008", "Drama", "7")
  list.append(Bad)

  search(list, Bad)
  get_series()
  print(series_list)
  get_movies()
  print(movies_list)

  print(Godfather)
  print(Peaky)
  Peaky.play()
  print(Peaky.views)
  print(list)
  