from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikatchu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.horizontal_char = "="
table.align = "l"
print(table)
