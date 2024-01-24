import requests

from heroes.hero.models import Hero

class Marvel_api():
    URL = "http://gateway.marvel.com/v1/public/characters"
    heroes = []
    heroes_response = []
    
    def build_url(self, *args, **kwargs):
        limit = kwargs.get('limit', 100)
        offset = kwargs.get('offset', 0)
        name = kwargs.get('name')
        pk = kwargs.get('pk')
        new_url = self.URL
        
        params = {
            "ts": "100",
            "apikey": "16e90537a937e7b409088e3f860ebab2",
            "hash": "107b7a9b68745b0157bb5e2def3130d8",
            "offset": offset,
            "limit": limit,
        }
        
        if name != None:
            params['nameStartsWith'] = name
        if pk != None:
            new_url = f'{self.URL}/{pk}'
                
        response = requests.get(
                new_url,
                params,
                verify=False
            )
        
        return response

    def get_all(self, params: dict):
        offset = params.get("offset", 0)
        limit = params.get("limit", 100)
        
        offset = int(offset)
        limit = int(limit)
        
        name = params.get("search")
        
        self.heroes = []
        while True:
            response = self.build_url(limit=limit, offset=offset, name=name)
            
            self.heroes.extend(response.json()['data']['results'])
            
            offset = offset + 100
            
            if response.json()['data']['count'] < 100:
                return self.build_response_heroes()
    
    def get_one(self, pk):
        self.heroes = []
        response = self.build_url(limit=100, offset=0, pk=pk)
        
        self.heroes.extend(response.json()['data']['results'])
        
        return self.build_response_heroes()
    
    def build_response_heroes(self):
        self.heroes_response = []
        for hero in self.heroes:
            hero_model = Hero()
            hero_model.id = hero['id']
            hero_model.name = hero['name']
            hero_model.description = hero['description']
            hero_model.image = hero['thumbnail']['path'] + '.' + hero['thumbnail']['extension']
            self.heroes_response.append(hero_model)
        return self.heroes_response
        