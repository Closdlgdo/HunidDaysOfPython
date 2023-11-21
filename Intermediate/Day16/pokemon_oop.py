from prettytable import PrettyTable

mesa = PrettyTable()
mesa.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
mesa.add_column('Type', ['Electric', 'Water', 'Fire'])

mesa.align = 'l'

print(mesa)
