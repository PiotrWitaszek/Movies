class Movies:
    def __init__(self, title, year, kind, views):
        self.title = title
        self.year = year
        self.kind = kind
        self.views = views

    def play(self):
        self.views = int(self.views + 1)
    
    def self(season):
        return '%02d' % self.season
    
    def self(episode):
        return '%02d' % self.episode
    
    def __str__(self):
        return f'{self.title} "S"{self.season}"E"{self.episode}'

    def __repr__(self):
        return f'{self.title} {self.year}'
        
class Series(Movies):
        def __init__(self, season, episode, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.season = season
            self.episode = episode        
