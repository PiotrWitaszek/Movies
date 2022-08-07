from faker import Faker
fake = Faker()
import random


class Movies:
    def __init__(self, title, year, kind, views):
        self.title = title
        self.year = year
        self.kind = kind
        self.views = views

    def play(self):
        self.views = self.views + 1
    
    
    def __str__(self):
        return f'{self.title} "S"{"%02d" % self.season}"E"{"%02d" % self.episode}'

    def __repr__(self):
        return f'{self.title} {self.year}'

     
    def get_kind():
        return random.choice(['Documentary', 'Thriller', 'Sci-Fi', 'Horror', 'Action', 'Comedy', 'Drama'])

    

        
class Series(Movies):
        def __init__(self, season, episode, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.season = season
            self.episode = episode        

        def get_season():
            return round(random.uniform(1, 10), 1)  

        def get_episode():
            return round(random.uniform(1, 20), 1)  

def create_library():
    print("Select the type:")
    print("m - movies")
    print("s - series")
    print("x - exit programm")
    while True:
            choice = input("Enter choice (m/s/x):")#ma być tak czy jedynie wprowadzam liczbę a program losowo generuje zarówno filmy jak i seraiale?

            if choice in ('m', 's',):
                quantity = int(input("Enter number of titles:"))
       
            if choice == 'm':
                library = []
                for i in range(quantity):
                    library.append(Movies(fake.word(), fake.year(), get_kind(), fake.number()))
                print(library)
            elif choice == 'b':
                library = []
                for i in range(quantity):
                   #czy moge tu wrzucać funkcje typu get_kind()? library.append(Series(fake.word(), fake.year(), fake.word(), fake.number(), fake.number(), fake.number())) 
                print(library)
            elif choice == 'x':
                exit()
            else:
                print("Invalid input")

if __name__ == "__main__":  
    create_library()

