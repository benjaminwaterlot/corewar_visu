class Champion():
	def __init__(self, id, name, description, process_count, color, pokemon,
	             big_pokemon):
		self.id = id
		self.name = name
		self.description = description
		self.process_count = process_count
		self.color = color
		self.pokemon = pokemon
		self.big_pokemon = big_pokemon
		self.victorious = False


class Process():
	def __init__(self, champion, location, pokemon):
		self.champion = champion
		self.location = location
		self.pokemon = pokemon
