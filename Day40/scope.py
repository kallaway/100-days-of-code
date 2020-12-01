################### Scope ####################
# this enemies is global
enemies = 1

def increase_enemies():
    # this one is local
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")