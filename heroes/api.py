import requests

from heroes.hero.models import Hero

class Marvel_api():
    URL = "http://gateway.marvel.com/v1/public/characters"
    heroes = []
    heroes_response = []

    def get_all(self):
        offset = 0
        while True:
            response = requests.get(
                self.URL,
                params={
                    "ts": "100",
                    "apikey": "16e90537a937e7b409088e3f860ebab2",
                    "hash": "107b7a9b68745b0157bb5e2def3130d8",
                    "offset": offset,
                    "limit": 100,
                },
                verify=False
            )
            
            self.heroes.extend(response.json()['data']['results'])
            
            offset = offset + 100
            
            if response.json()['data']['count'] < 100:
                return self.build_list_heroes()
    
    def build_list_heroes(self):
        for hero in self.heroes:
            hero_model = Hero()
            hero_model.id = hero['id']
            hero_model.name = hero['name']
            hero_model.description = hero['description']
            hero_model.image = hero['thumbnail']['path'] + '.' + hero['thumbnail']['extension']
            self.heroes_response.append(hero_model)
        return self.heroes_response
        