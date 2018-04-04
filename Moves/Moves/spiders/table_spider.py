import scrapy

MOVES = {}
class QuotesSpider(scrapy.Spider):
    name = 'pokenames'
    start_urls = ['https://pokemondb.net/pokedex/national']

    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url, self.parse_pokemons)

    def parse_pokemons(self, response):
        names = []
        dex = []
        pokemons = response.css('.infocard-tall-list .infocard-tall')
        for pokemon in pokemons:
            name = pokemon.css('.ent-name::text').extract_first()


            names.append(name)
        ### at this point, we will have a list of all pokemons names, called names

        # STEP 2
        
        # we will create a new URL for each pokemon in the pokemons list
        i = 1
        base_url = "https://pokemondb.net/pokedex/"
        for name in names[:251]:
            if name == "Farfetch'd":
                name = "farfetchd"
            elif name == 'Mr. Mime':
                name = "mr-mime"
            elif name == 'Nidoran♂':
                name = 'Nidoran-m'
            elif name == 'Nidoran♀':
                name = 'Nidoran-f'
            elif name == 'Mime Jr.':
                name = 'mime-jr'
            elif name == 'Flabébé':
                name = 'flabebe'
            elif name == 'Type: Null':
                name = 'type-null'
            elif name == 'Tapu Koko':
                name = 'tapu-koko'
            elif name == 'Tapu Lele':
                name = 'tapu-lele'
            elif name == 'Tapu Bulu':
                name = 'tapu-bulu'
            elif name == 'Tapu Fini':
                name = 'tapu-fini'

            url = base_url + name.lower().replace(' ','')
            yield scrapy.Request(url, self.parse_pokemon)
    
# MOVES = {'Bulbasaur': {moves_for_pokemon},"Ivysaur":},

    def parse_pokemon(self, response):
        MOVE_TYPES = ["Level", "Egg", "Tutor", "TM", "Name"]
        all_moves = response.css(".wide-table")
        ultra_series_moves = all_moves[:4]

        name = response.xpath('/html/body/article/h1//text()').extract_first()

        moves_for_pokemon = {}
        for i, selector in enumerate(ultra_series_moves):
            sub_moves = []
            rows = selector.css("tbody tr")
            for row in rows:
                if i == 0:
                    move_level = row.css("td.num::text").extract_first()
                    move_name = row.css("td a.ent-name::text").extract_first()
                    move = {'level': move_level, 'name': move_name}
                elif i == 1:
                    move_name = row.css("td a.ent-name::text").extract_first()
                    move = {'name': move_name}
                elif i == 2:
                    move_name = row.css("td a.ent-name::text").extract_first()
                    move = {'name': move_name}
                else:
                    # i == 3
                    tm = row.css("td.num::text").extract_first()
                    move_name = row.css("td a.ent-name::text").extract_first()
                    move = {'tm': tm, 'name': move_name}
                sub_moves.append(move)
            moves_for_pokemon[MOVE_TYPES[i]] = sub_moves

        MOVES[name] = moves_for_pokemon






