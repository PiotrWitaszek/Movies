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
#czy zamiast value ma być coś w stylu self.title?
def get_series():
  for elem in list:
    if isinstance(elem, Series):
      series_list.append(elem)
  return series_list

def get_movies():
  for elem in list:
    if isinstance(elem, Series) == False:
       movies_list.append(elem)
  return movies_list
#if elem(type(Movies)) == True:
 #      mniej więcej tak wykorzystać tego type() - wiem, że mniej bo nie wychodzi
  
      
  
if __name__ == '__main__':
  list = [] 
  series_list = []
  movies_list = []
  Shawshank = Movies("Shawshank redemption", "1994", "Drama", "22")
  list.append(Shawshank)
  # snake_case chodzi o cos takiego shawshank_redemption?
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