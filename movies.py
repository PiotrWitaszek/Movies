
list = []

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

Shawshank = Movies("Shawshank redemption", "1994", "Drama", "22")
list.append(Shawshank)
Godfather = Movies("The Godfather", "1972", "Drama", "24")
list.append(Godfather)
Psycho = Movies("Psycho", "1960", "Thriller", "19")
list.append(Psycho)
Requiem = Movies("Requiem for a dream", "2000", "Drama", "14")
list.append(Requiem)

           
class Series(Movies):
        def __init__(self, season, episode, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.season = season
            self.episode = episode        
        def __str__(self):
          return f"{self.title} S{int(self.season):02d}E{int(self.episode):02d}"

Peaky = Series("1", "4", "Peaky Blinders", "2013", "Drama", "22")
list.append(Peaky)
Bad = Series("3", "9", "Breaking Bad", "2008", "Drama", "7")
list.append(Bad)

  

print(Godfather)
print(Peaky)
Peaky.play()
print(Peaky.views)
print(list)

#parę pytań:
#funkcja search - czy ma to działać z inputem, czy jakoś w stylu find()?
#get_movies i get_series - isinstance?
# list.append zrobić jakimś for in range?
