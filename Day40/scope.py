################### Scope ####################
# this enemies is global
# enemies = 1

# def increase_enemies():
#     # this one is local
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# Global Scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

# No block scope in Python
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

# print(new_enemy)

# Modifying the Global Scope
enemies = 1

def increase_enemies():
    # have to add global name to variable. Avoid modifying within a function
    # global enemies 
    # enemies += 1
    print(f"Enemies inside function: {enemies}")
    # use return instead
    return enemies + 1

increase_enemies()
print(f"Enemies outside function: {enemies}")
