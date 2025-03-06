import random

class Country:

    terrain = "land"

    def __init__(self, name, population, language, in_europe = False):
        self.name = name
        self.population = population
        self.language = language
        self.in_europe = in_europe
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, in_str):
        if in_str:
            self._name = in_str
        else:
            raise ValueError("name can not be blank")
    
    @name.deleter
    def name():
        raise ValueError("name can not be deleted")
    
    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, num):
        if num >= 0:
            self._population = num
        else:
            raise ValueError("population can not be less than 0")
    
    @population.deleter
    def population(self):
        raise ValueError("population can not be deleted")
    
    @property
    def in_europe(self):
        return self._in_europe
    
    @in_europe.setter
    def in_europe(self, new_in = False):
        if isinstance(new_in, bool):
            self._in_europe = new_in
        else:
            raise ValueError("in_europe must be a boolan")

    @in_europe.deleter
    def in_europe(self):
        raise ValueError("in_europe can not be deleted")
    
    def grow_pop(self, rate):
        if isinstance(rate, float) and -1 < rate < 1:
            # self.population += self.population * rate

            # The above adjustment is too drastic -- populations always crash to nearly 0
            # So, many we can minimize the shrink by only applying the rate to 10% of the population?
            self.population += (self.population * 0.10) * rate
    
    def show_lore(self):
        print(f"{self.name} is a {self.terrain}-based entity with {self.population} souls.")

    @staticmethod
    def show_kind():
        print("All countries are based on " + Country.terrain)
    

belgium = Country("Belgium", 11_697_557, "Flemish", True)
france = Country("France", 68_373_433, "French", True)
spain = Country("Spain", 48_592_909, "Spanish", True)
portugal = Country("Portugal", 10_467_366, "Portuguese", True)
india = Country("India", 1_428_627_663, "Hindi")

all_countries = [belgium, france, spain, portugal, india]

for country in all_countries:
    country.initial_population = country.population

for year in range(1000):
    for country in all_countries:
        growth_rate = random.uniform(-1, 1)
        country.grow_pop(growth_rate)
        # print(f"=== {country.name} after {year + 1} years: ({growth_rate}) {country.population} ===")

print("=== Population after 1000 years ===")
for country in all_countries:
    print(f"{country.name}: {country.population}")

print()
print("Highest population country")
highest = 0
high_country = None
for country in all_countries:
    if country.population > highest:
        highest = country.population
        high_country = country
high_country.show_lore()

print("Alternate max:")
(max(all_countries, key=lambda c: c.population)).show_lore()

print()
print("Countries that grew larger than initial population:")
big_countries = filter(lambda c: c.in_europe and c.population > c.initial_population, all_countries)
for country in big_countries:
    country.show_lore()

print()
print("Changing Country terrain")
Country.terrain = "water"
print("Country.terrain:", Country.terrain)
all_countries[-1].show_lore()

print()
print("Changing just the last country")
all_countries[-1].terrain = 'fire'
print("Last country is now:", all_countries[-1].terrain)
Country.show_kind()
