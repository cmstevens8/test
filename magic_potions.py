potions = { "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"] }

print("Available potions:")
for potion in potions:
    print(potion)

chosen_potion = input("Chose a potion: ") 

if chosen_potion in potions:
    ingredients = potions[chosen_potion]
    print("Ingredients for", chosen_potion)

    i = 0
    while i < len(ingredients):
        print(f"Do you want to buy {ingredients[i]}? (yes/no)")
        choice = input()

        if choice == "yes":
            print(f"Great! You've bought {ingredients[i]}.")
            i += 1  
        elif choice == "no":
            print(f"You've decided to stop shopping.")
            break  
        else:
            print("Please enter 'yes' or 'no'.")

        if i == len(ingredients):
            print(f"\nYou've bought all the ingredients for {chosen_potion}!")