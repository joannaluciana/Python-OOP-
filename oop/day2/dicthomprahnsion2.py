
accounts = { 'Artur':10, "Karolina":1000, "Michał":1000}

new_accounts = { name:balance * 1.01 for (name, balance) in accounts.items()}
print(new_accounts)

# MAP
new_accounts2 = list(map (lambda items :( items[0],items[1] * 1.01), accounts.items()))
print(new_accounts2)

#MAP li