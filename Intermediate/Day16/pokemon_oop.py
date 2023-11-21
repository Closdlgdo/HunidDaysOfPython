from prettytable import PrettyTable

mesa = PrettyTable()
mesa.add_column('Pokemon Name', ['Raichu', 'Venasaur', 'Blastoise', 'Charizard'])
mesa.add_column('Type', ['Electric', 'Grass/Poison', 'Water', 'Fire'])
mesa.add_column('Poke-move', ['Thunder', 'Solar Beam', 'Hydro-Pump', 'Fire-Blast'])

mesa.align = 'c'

print(mesa)
