# --- Base Products ---
base_products = {
    'OG Kush': 'Calming',
    'Sour Diesel': 'Refreshing',
    'Green Crack': 'Energizing',
    'Grandaddy Purple': 'Sedating',
    'Meth': None,
    'Cocaine': None
}

# --- Effects Mapping ---
effects_mapping = {
    ('Banana', 'Smelly'): 'Anti-Gravity',
    ('Paracetamol', 'Munchies'): 'Anti-Gravity',
    ('Mouth Wash', 'Calming'): 'Anti-Gravity',
    ('Motor Oil', 'Paranoia'): 'Anti-Gravity',
    ('Cuke', 'Munchies'): 'Athletic',
    ('Cuke', 'Slippery'): 'Athletic',
    ('Paracetamol', 'Electrifying'): 'Athletic',
    ('Paracetamol', 'Paranoia'): 'Balding',
    ('Paracetamol', 'Energizing'): 'Balding',
    ('Energy Drink', 'Schizophenic'): 'Balding',
    ('Paracetamol', 'Spicy'): 'Bright-Eyed',
    ('V*agra', 'Euphoric'): 'Bright-Eyed',
    ('Flu Medicine', 'Calming'): 'Bright-Eyed',
    ('Chili', 'Sneaky'): 'Bright-Eyed',
    ('Paracetamol', 'Foggy'): 'Calming',
    ('V*agra', 'Laxative'): 'Calming',
    ('Flu Medicine', 'Focused'): 'Calming',
    ('Gasoline', 'Paranoia'): 'Calming',
    ('Mega Bean', 'Sneaky'): 'Calming',
    ('Horse S*men', 'Anti-Gravity'): 'Calming',
    ('Battery', 'Laxative'): 'Calorie-Dense',
    ('Cuke', 'Foggy'): 'Cyclopean',
    ('Mega Bean', 'Thought-Provoking'): 'Cyclopean',
    ('Mega Bean', 'Energizing'): 'Cyclopean',
    ('Gasoline', 'Electrifying'): 'Disorienting',
    ('Mega Bean', 'Focused'): 'Disorienting',
    ('Energy Drink', 'Glowing'): 'Disorienting',
    ('Mega Bean', 'Shrinking'): 'Electrifying',
    ('Energy Drink', 'Disorienting'): 'Electrifying',
    ('Addy', 'Long-Faced'): 'Electrifying',
    ('Horse S*men', 'Thought-Provoking'): 'Electrifying',
    ('Donut', 'Shrinking'): 'Energizing',
    ('Mega Bean', 'Thought-Provoking'): 'Energizing',
    ('Energy Drink', 'Euphoric'): 'Energizing',
    ('Addy', 'Foggy'): 'Energizing',
    ('Cuke', 'Toxic'): 'Euphoric',
    ('Donut', 'Focused'): 'Euphoric',
    ('Flu Medicine', 'Laxative'): 'Euphoric',
    ('Gasoline', 'Energizing'): 'Euphoric',
    ('Energy Drink', 'Spicy'): 'Euphoric',
    ('Chili', 'Athletic'): 'Euphoric',
    ('Battery', 'Electrifying'): 'Euphoric',
    ('Addy', 'Explosive'): 'Euphoric',
    ('Donut', 'Calorie-Dense'): 'Explosive',
    ('Banana', 'Disorienting'): 'Focused',
    ('Gasoline', 'Shrinking'): 'Focused',
    ('Mega Bean', 'Seizure-Inducing'): 'Focused',
    ('Flu Medicine', 'Cyclopean'): 'Foggy',
    ('Gasoline', 'Laxative'): 'Foggy',
    ('Donut', 'Jennerising'): 'Gingeritis',
    ('Paracetamol', 'Focused'): 'Gingeritis',
    ('Flu Medicine', 'Thought-Provoking'): 'Gingeritis',
    ('Iodine', 'Calorie-Dense'): 'Gingeritis',
    ('Addy', 'Sedating'): 'Gingeritis',
    ('Gasoline', 'Disorienting'): 'Glowing',
    ('Mega Bean', 'Calming'): 'Glowing',
    ('Mega Bean', 'Sneaky'): 'Glowing',
    ('Battery', 'Cyclopean'): 'Glowing',
    ('Banana', 'Paranoia'): 'Jennerising',
    ('Mouth Wash', 'Focused'): 'Jennerising',
    ('Cuke', 'Euphoric'): 'Laxative',
    ('Energy Drink', 'Foggy'): 'Laxative',
    ('Mega Bean', 'Athletic'): 'Laxative',
    ('Chili', 'Laxative'): 'Long-Faced',
    ('Cuke', 'Slippery'): 'Munchies',
    ('Flu Medicine', 'Athletic'): 'Munchies',
    ('Energy Drink', 'Sedating'): 'Munchies',
    ('Motor Oil', 'Energizing'): 'Munchies',
    ('Battery', 'Shrinking'): 'Munchies',
    ('Cuke', 'Sneaky'): 'Paranoia',
    ('Paracetamol', 'Energizing'): 'Paranoia',
    ('Flu Medicine', 'Shrinking'): 'Paranoia',
    ('Mega Bean', 'Jennerising'): 'Paranoia',
    ('Iodine', 'Foggy'): 'Paranoia',
    ('Banana', 'Long-Faced'): 'Refreshing',
    ('Flu Medicine', 'Electrifying'): 'Refreshing',
    ('Chili', 'Shrinking'): 'Refreshing',
    ('Addy', 'Glowing'): 'Refreshing',
    ('Horse S*men', 'Gingeritis'): 'Refreshing',
    ('Motor Oil', 'Energizing'): 'Schizophrenic',
    ('Motor Oil', 'Munchies'): 'Schizophrenic',
    ('Iodine', 'Calming'): 'Sedating',
    ('Mouth Wash', 'Explosive'): 'Sedating',
    ('Gasoline', 'Munchies'): 'Sedating',
    ('Motor Oil', 'Euphoric'): 'Sedating',
    ('Banana', 'Focused'): 'Seizure-Inducing',
    ('Iodine', 'Euphoric'): 'Seizure-Inducing',
    ('Energy Drink', 'Focused'): 'Shrinking',
    ('Paracetamol', 'Calming'): 'Slippery',
    ('Donut', 'Anti-Gravity'): 'Slippery',
    ('Flu Medicine', 'Munchies'): 'Slippery',
    ('Banana', 'Toxic'): 'Smelly',
    ('Gasoline', 'Gingeritis'): 'Smelly',
    ('Banana', 'Calming'): 'Sneaky',
    ('Donut', 'Balding'): 'Sneaky',
    ('V*agra', 'Athletic'): 'Sneaky',
    ('Mouth Wash', 'Calorie-Dense'): 'Sneaky',
    ('Gasoline', 'Jennerising'): 'Sneaky',
    ('Energy Drink', 'Trophic Thunder'): 'Sneaky',
    ('Iodine', 'Toxic'): 'Sneaky',
    ('Gasoline', 'Energizing'): 'Spicy',
    ('Gasoline', 'Euphoric'): 'Spicy',
    ('Cuke', 'Gingeritis'): 'Thought-Provoking',
    ('Banana', 'Cyclopean'): 'Thought-Provoking',
    ('Banana', 'Energizing'): 'Thought-Provoking',
    ('Iodine', 'Refreshing'): 'Thought-Provoking',
    ('Paracetamol', 'Glowing'): 'Toxic',
    ('V*agra', 'Disorienting'): 'Toxic',
    ('Chili', 'Munchies'): 'Toxic',
    ('Mega Bean', 'Slippery'): 'Toxic',
    ('Motor Oil', 'Foggy'): 'Toxic',
    ('Flu Medicine', 'Euphoric'): 'Toxic',
    ('Paracetamol', 'Toxic'): 'Tropic Thunder',
    ('Gasoline', 'Sneaky'): 'Tropic Thunder',
    ('Chili', 'Anti-Gravity'): 'Tropic Thunder',
    ('Battery', 'Munchies'): 'Tropic Thunder',
    ('Battery', 'Euphoric'): 'Zombifying'
}

# (rest of your code continues unchanged)

# --- Correct Pathfinding Function (Real Chain Simulation Updated) ---
def find_ingredient_path_simulated_real(starting_product, desired_effects):
    from collections import deque

    MAX_NODES = 1_000_000
    nodes_visited = 0

    # Start with initial traits and effects
    initial_traits = set()
    initial_effects = set()
    if base_products[starting_product]:
        initial_traits.add(base_products[starting_product])
        initial_effects.add(base_products[starting_product])

    queue = deque()
    queue.append((initial_traits, initial_effects, []))  # (traits, effects, path)

    visited = set()
    visited.add((frozenset(initial_traits), frozenset(initial_effects)))

    while queue:
        current_traits, current_effects, path = queue.popleft()
        nodes_visited += 1

        if nodes_visited >= MAX_NODES:
            print(f"\n❌ Reached {MAX_NODES} paths explored. Stopping search.")
            return None

        if desired_effects.issubset(current_effects):
            print(f"\n✅ Found a path after visiting {nodes_visited} paths!")
            return path

        # Try applying any ingredient that matches (Ingredient, TraitToReplace)
        for (ingredient, trait_to_replace), unlocks_effect in effects_mapping.items():
            if trait_to_replace not in current_traits:
                continue  # Can't replace a trait we don't have

            new_traits = current_traits.copy()
            new_effects = current_effects.copy()

            new_traits.discard(trait_to_replace)
            new_traits.add(unlocks_effect)
            new_effects.add(unlocks_effect)

            frozen_new_traits = frozenset(new_traits)
            frozen_new_effects = frozenset(new_effects)

            if (frozen_new_traits, frozen_new_effects) in visited:
                continue  # Already visited this combination

            visited.add((frozen_new_traits, frozen_new_effects))
            new_path = path + [(ingredient, unlocks_effect)]
            queue.append((new_traits, new_effects, new_path))

    print(f"\n❌ No valid path found. Visited {nodes_visited} paths.")
    return None


# --- CLI Interface ---
def cli_interface():
    print("\nWelcome to the Schedule 1 Effects Mixer!\n")

    # Select starting product
    print("Choose your starting product:")
    base_products_list = list(base_products.keys())
    for idx, product in enumerate(base_products_list, 1):
        print(f"{idx}. {product}")

    product_choice = int(input("\nEnter the number of your choice: ")) - 1
    starting_product = base_products_list[product_choice]
    starting_effect = base_products[starting_product]

    print(f"\nYou selected: {starting_product} with starting effect: {starting_effect}")

    # Select desired effects
    print("\nAvailable Effects:")
    effects_list = sorted(set(effect for (_, _), effect in effects_mapping.items()))
    for idx, effect in enumerate(effects_list, 1):
        print(f"{idx}. {effect}")

    desired_effects_input = input("\nEnter the numbers of your desired effects (comma-separated): ")
    desired_effects_indices = [int(idx.strip()) - 1 for idx in desired_effects_input.split(',')]
    desired_effects = {effects_list[i] for i in desired_effects_indices}

    print("\nFinding path to your effects...")

    path = find_ingredient_path_simulated_real(starting_product, desired_effects)

    if path:
        print("\nMix the following ingredients in this order:")
        for idx, (ingredient, unlocks_effect) in enumerate(path, 1):
            print(f"{idx}. Add {ingredient} → Unlocks {unlocks_effect}")
    else:
        print("\n❌ No valid path found from the starting product to achieve all desired effects!")

# --- Run it ---
cli_interface()
