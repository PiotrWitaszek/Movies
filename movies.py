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
    if elem.title == value:
      return elem
  return False
       
def get_series(list):
  for elem in list:
    if type(elem) == Series:
      series_list.append(elem)
  return series_list

def get_movies(list):
  for elem in list:
    if type(elem) == Movies:
       movies_list.append(elem)
  return movies_list
  
  
if __name__ == '__main__':
  list = [] 
  series_list = []
  movies_list = []
  shawshank = Movies("Shawshank_redemption", 1994, "Drama", 22)
  list.append(shawshank)
  godfather = Movies("The_Godfather", 1972, "Drama", 24)
  list.append(godfather)
  psycho = Movies("Psycho", 1960, "Thriller", 19)
  list.append(psycho)
  requiem = Movies("Requiem_for_a_dream", 2000, "Drama", 14)
  list.append(requiem) 
  peaky = Series(1, 4, "Peaky_Blinders", 2013, "Drama", 22)
  list.append(peaky)
  bad = Series(3, 9, "Breaking_Bad", 2008, "Drama", 7)
  list.append(bad)

  print(search(list, "Breaking_Bad"))
  get_series(list)
  print(series_list)
  get_movies(list)
  print(movies_list)

  print(godfather)
  print(peaky)
  peaky.play()
  print(peaky.views)
  print(list)
  