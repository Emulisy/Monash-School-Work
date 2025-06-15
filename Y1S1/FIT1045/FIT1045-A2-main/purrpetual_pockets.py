""" 
Team: Applied5 
Student Names: Justin Wong, Ian Zhang
Date: January 6, 2025
"""

############## DISPLAY GRID ##############

def display_grid(grid_dictionary: dict) -> None:
    # Square root to get rows and cols
    length = int(len(grid_dictionary) ** 0.5)
    # Iterate through the dictionary
    for row in range(length):
        # Print vibe
        for column in range(length):
            if "vibe" not in grid_dictionary[column + 1 + row * length]:
                print("₍>._.<₎", end="")
            elif grid_dictionary[column + 1 + row * length]["vibe"] == "full":
                print("₍˄.ˬ.˄₎", end="")
            elif grid_dictionary[column + 1 + row * length]["vibe"]  == "hangry":
                print("₍˅¤_¤˅₎", end="")
            elif grid_dictionary[column + 1 + row * length]["vibe"]  == "neutral":
                print("₍>._.<₎", end="")
        print()

        # Print cell
        for column in range(length):
            if "player" in grid_dictionary[column + 1 + row * length]:
                print(f"(  {grid_dictionary[column + 1 + row * length]["player"][0]}  )", end="")
            elif "position" in grid_dictionary[column + 1 + row * length]:
                print(f"(  {grid_dictionary[column + 1 + row * length]["position"]:<2} )", end="")
            else:
                print("(     )", end="")
        print()

#add any other Task 1 helper functions here
    
############## ACQUIRE FOOD ##############

def acquire_food(food_options_file: str, ingredients_file: str) -> dict:
    def read_csv(file_name):
        array = [] # Array of dictionaries as rows with headers as keys
        delimiter = None
        
        with open(file_name, "r") as file:
            # Identify the delimiter
            headers = file.readline().strip()
            for char in headers:
                if not char.isalpha() and char not in [",", " ", "(", ")"]:
                    delimiter = char
                    break
            # Update headers to be a list of strings
            headers = headers.split(delimiter)

            # Read the remaining lines
            for line in file: # each row
                dictionary = {}
                values = line.strip().split(delimiter)

                for i in range(len(headers)): # each column
                    if values[i].replace(".", "").isdigit():
                        dictionary[headers[i]] = float(values[i]) # add the value to the dictionary
                    else:
                        dictionary[headers[i]] = values[i]
                array.append(dictionary) # add the dictionary to the array
        return array

    # Read files to arrays
    food_options_data = read_csv(food_options_file)
    ingredients_data = read_csv(ingredients_file)

    # Create a dictionary to store the final result
    result = {}

    # Iterate through the food options data
    for food_option in food_options_data:
        # Extract the portion size
        portion = food_option["Portion (g)"]

        # Extract the top 3 ingredients
        ingredients = food_option["Main Ingredients (Top 3)"].split(", ")

        # Extract the type
        food_type = food_option["Type"]

        # Calculate the actual nutritional values
        calories = 0
        carbohydrates = 0
        sugars = 0
        protein = 0
        fat = 0

        for ingredient in ingredients:
            # Extract the ingredient data
            ingredient_data = next((data for data in ingredients_data if data["Ingredient"] == ingredient), None)

            # Calculate the actual portion of the ingredient
            actual_portion = portion * (40 if ingredient == ingredients[0] else 25 if ingredient == ingredients[1] else 15) / 100

            # Calculate the actual nutritional values
            calories += ingredient_data["Calories (kcal)"] / 100 * actual_portion
            carbohydrates += ingredient_data["Carbohydrates (g)"] / 100 * actual_portion
            sugars += ingredient_data["Sugars (g)"] / 100 * actual_portion
            protein += ingredient_data["Protein (g)"] / 100 * actual_portion
            fat += ingredient_data["Fat (g)"] / 100 * actual_portion

        # Round the values to 4 decimal places
        calories = round(calories, 4)
        carbohydrates = round(carbohydrates, 4)
        sugars = round(sugars, 4)
        protein = round(protein, 4)
        fat = round(fat, 4)

        # Add the food option to the result
        result[food_option["Code"]] = {
            "Food Name": food_option["Food Name"],
            "Type": food_type,
            "Portion": int(portion),
            "Calories": calories,
            "Carbohydrates": carbohydrates,
            "Sugars": sugars,
            "Protein": protein,
            "Fat": fat
        }

    return result

#add any other Task 2 helper functions here

############## PURRSON-RELATED ##############

class Purrson:
    INITIAL_POCKET_SPACE = 1500
    INITIAL_CALORIES = 5000
    INITIAL_VIBE = "neutral"
    
    # Constructor method
    def __init__(self, name: str, food_dictionary: dict):
        self.name = name
        self.pocket_space = Purrson.INITIAL_POCKET_SPACE
        self.pocket_content = []
        self.calories = float(Purrson.INITIAL_CALORIES)
        self.grid_positions = []
        self.vibe = Purrson.INITIAL_VIBE
        self.food_dictionary = food_dictionary

    # Getter methods
    def get_name(self):
        return self.name
    
    def get_pocket_space(self):
        return self.pocket_space
    
    def get_pocket_content(self):
        return self.pocket_content
    
    def get_calories(self):
        return int(self.calories)
    
    def get_grid_positions(self):
        return self.grid_positions
    
    def get_vibe(self):
        return self.vibe
    
    def get_food_dictionary(self):
        return self.food_dictionary
    
    # Update methods
    def update_calories_pocket_space(self, calories: int, pocket_space: int):
        self.calories += calories
        self.pocket_space += pocket_space

    def update_pocket_content(self, food_item: str):
        self.pocket_content.append(food_item)

    def update_grid_position(self, new_grid_position: int):
        self.grid_positions.append(new_grid_position)

    def get_current_grid_position(self):
        return self.grid_positions[-1] if self.grid_positions else None
    
    def update_vibe(self, vibe: str):
        self.vibe = vibe
    
    def revert_state(self, num: int):
        if num >= len(self.grid_positions):
            self.grid_positions = []
            self.pocket_content = []
        else:
            self.grid_positions = self.grid_positions[:-num]
            self.pocket_content = self.pocket_content[:-num]

    # String representation methods
    def __str__(self):
        return f"{self.get_vibe().capitalize()} {self.get_name()} has collected {len(self.get_pocket_content())} food items and has {self.get_pocket_space()} / {Purrson.INITIAL_POCKET_SPACE} pocket space left."
    
    def __repr__(self):
        return self.__str__()
    
    # Additional methods
    def get_next_grid_positions(self, grid: dict) -> list:
        length = int(len(grid) ** 0.5)
        current_position = self.get_current_grid_position()
        next_positions = []
        # Corners
        if current_position == 1:
            next_positions = [2, length + 1]
        elif current_position == length: # top right
            next_positions = [1, length ** 2]
        elif current_position == length ** 2 - length + 1: # bottom left
            next_positions = [1, length ** 2]
        elif current_position == length ** 2:
            next_positions = [length ** 2 - length, length ** 2 - 1]
        # Edges
        elif current_position % length == 1: # left edge
            next_positions = [current_position - length, current_position + 1, current_position + length]
        elif current_position < length: # top edge
            next_positions = [current_position - 1, current_position + 1, current_position + length]
        elif current_position % length == 0: # right edge
            next_positions = [current_position - length, current_position - 1, current_position + length]
        elif current_position > length ** 2 - length + 1: # bottom edge
            next_positions = [current_position - length, current_position - 1, current_position + 1]
        else: # middle
            next_positions = [current_position - length, current_position - 1, current_position + 1, current_position + length]
        return next_positions
    
    def display_pocket_content(self) -> None:
        print(f"+++ {self.get_name().upper()}'S POCKET CONTENT +++")
        food_type_list = {"Decadent Desserts": [], "Healthy Treats": []}

        name_length = 0
        for food in self.get_pocket_content():
            if self.get_food_dictionary()[food]["Type"] == "Decadent Dessert": # csv file has no s behind dessert
                food_type_list["Decadent Desserts"].append(food)
            elif self.get_food_dictionary()[food]["Type"] == "Healthy Treats":
                food_type_list["Healthy Treats"].append(food)
            name_length = max(name_length, len(self.get_food_dictionary()[food]["Food Name"]))

        if not food_type_list["Decadent Desserts"] and not food_type_list["Healthy Treats"]:
            print("No Food Items Consumed\n")
        else:
            for food_type in food_type_list:
                if not food_type_list[food_type]:
                    continue
                else:
                    food_type_list[food_type].sort(key=lambda x: self.get_pocket_content().index(x))
                    print(food_type)
                    print(f"No. {"Food Name":<{name_length}} Portion")
                    for i, food in enumerate(food_type_list[food_type]):
                        print(f"[{i + 1}] {self.get_food_dictionary()[food]['Food Name']:<{name_length}} {self.get_food_dictionary()[food]['Portion']:>5} g")
                    print()
            
        print("+++ TOTAL NUTRITIONAL VALUES +++")

        # Calculate total nutritional values
        totals_dictionary = self.calculate_total()

        print(f"Calories               {round(totals_dictionary["Calories"]):>5} kcal")
        print(f"Carbohydrates          {round(totals_dictionary["Carbohydrates"]):>5} g")
        print(f"Fat                    {round(totals_dictionary["Fat"]):>5} g")
        print(f"Protein                {round(totals_dictionary["Protein"]):>5} g")
        print(f"Sugars                 {round(totals_dictionary["Sugars"]):>5} g") # NOTE no \n here

    def met_win_conditions(self, minimum: dict) -> bool:
        has_won = True
        totals_dictionary = self.calculate_total()
        for nutrient in minimum:
            if totals_dictionary[nutrient] < minimum[nutrient]:
                has_won = False
                break
        return has_won

    # Helper method
    def calculate_total(self):
        totals_dictionary = {"Calories": 0, "Carbohydrates": 0, "Fat": 0, "Protein": 0, "Sugars": 0}
        for food in self.get_pocket_content():
            for nutrient in totals_dictionary:
                totals_dictionary[nutrient] += self.get_food_dictionary()[food][nutrient]
        
        return totals_dictionary

#add any other Purrson related classes and functions here

############## GAMEGRID-RELATED #############

class GameGrid:
    INITIAL_VIBE = "neutral"
    FOOD_TYPE_LIST = ["Decadent Dessert", "Healthy Treats"]

    # Constructor method
    def __init__(self, grid_position: int, grid_dictionary: dict, food_dictionary: dict):
        self.grid_position = grid_position
        self.food_type = "No Food Type"
        self.food_items = [] # List of food codes
        self.vibe = GameGrid.INITIAL_VIBE

        # Assign food type
        length = int(len(grid_dictionary) ** 0.5)
        if grid_position != length and grid_position != length ** 2 - length + 1 and grid_position != (length ** 2 + 1) // 2:
            if grid_position % 2 == 1:
                self.food_type = GameGrid.FOOD_TYPE_LIST[0]
            elif grid_position % 2 == 0:
                self.food_type = GameGrid.FOOD_TYPE_LIST[1]
        
        # Add food items
        for key, value in food_dictionary.items():
            if value["Type"] == self.food_type:
                self.add_food_item(key)

        # Add to grid dictionary
        grid_dictionary[grid_position]["grid object"] = self
            
    # Getter methods
    def get_grid_position(self):
        return self.grid_position
    
    def get_food_type(self):
        return self.food_type
    
    def get_food_items(self):  
        return self.food_items
    
    def get_vibe(self):
        return self.vibe
    
    # Update methods
    def set_food_type(self, food_type: str):
        self.food_type = food_type

    def add_food_item(self, food_item: str):
        self.food_items.append(food_item)

    def remove_food_item(self, food_item: str):
        self.food_items.remove(food_item)

    # Display food items
    def display_food_items(self, food_dictionary: dict, pocket_space: int):
        print(f"\nPosition {self.get_grid_position()}: {self.get_food_type()} Grid [{len(self.get_food_items())} Food Items Available]")
        
        # Check for food items that fit in pocket space
        valid_food_items = []
        name_length = 0
        for food_item in self.get_food_items():
            if len(valid_food_items) >= 5:
                break
            if food_dictionary[food_item]["Portion"] <= pocket_space:
                valid_food_items.append(food_item)
                name_length = max(name_length, len(food_dictionary[food_item]["Food Name"]))

        # Display food items
        if len(valid_food_items) == 0:
            print("No Food Items fit Pocket Space")
        else:
            print(f"No. {"Food Name":<{name_length}} Portion")
            for i, food_item in enumerate(valid_food_items):
                food_name = food_dictionary[food_item]["Food Name"]
                portion = food_dictionary[food_item]["Portion"]
                print(f"[{i + 1}] {food_name:<{name_length}} {portion:>5} g")

    # Magic methods
    def __str__(self):
        return f"Position {self.get_grid_position()}: {self.get_food_type()} Grid [{len(self.get_food_items())} Food Items Available]"

    def __repr__(self):
        return self.__str__()

#add any other GameGrid related classes and functions here
class PurrsperityGrid(GameGrid):

    # Constructor method
    def __init__(self, grid_position: int, grid_dictionary: dict, food_dictionary: dict):
        super().__init__(grid_position, grid_dictionary, food_dictionary)
        self.food_type = "Special Food"

        # Special food items
        self.food_items = ["Double Pocket Space", "Replenish Calories", "Diminish Opponent's Calories", "Revert Opponent", "Double Last Food Item"]

    # Select special food item method
    def select_special_food_item(self, player: Purrson, opponent: Purrson):
        print()
        print(self)
        for i, food_item in enumerate(self.get_food_items()):
            print(f"[{i + 1}] {food_item}")
        
        # User input
        choice = self.get_food_items()[int(input("\nSelect an item to consume: ")) - 1]
        print(f"{player.get_name()} gains the ability to {choice}.\n")

        # Double Pocket Space FIX THIS
        if choice == "Double Pocket Space":
            player.update_calories_pocket_space(0, Purrson.INITIAL_POCKET_SPACE)
            print(f"UPDATE: {player.get_vibe().capitalize()} {player.get_name()} has collected {len(player.get_pocket_content())} food items and has {player.get_pocket_space()} / {Purrson.INITIAL_POCKET_SPACE * 2} pocket space left.")
            self.remove_food_item(choice)
        # Replenish Calories
        elif choice == "Replenish Calories":
            player.calories = Purrson.INITIAL_CALORIES
            print(f"UPDATE: {player.get_vibe().capitalize()} {player.get_name()}'s calories is back to {Purrson.INITIAL_CALORIES}.\n")
            self.remove_food_item(choice)
        # Diminish Opponent's Calories
        elif choice == "Diminish Opponent's Calories":
            opponent.calories /= 2
            print(f"UPDATE: {opponent.get_vibe().capitalize()} {opponent.get_name()}'s calories is down to {int(opponent.calories)}.")
            self.remove_food_item(choice)
        # Revert Opponent
        elif choice == "Revert Opponent":
            print("BEFORE:")
            opponent.display_pocket_content()
            print(f"\n+++ {opponent.get_name().upper()}'S GRID POSITIONS +++")
            print(opponent.get_grid_positions())

            option = int(input(f"\nSelect one option [1] Revert {opponent.get_name()}'s last item, [2] Revert {opponent.get_name()} last 2 items, [3] Revert {opponent.get_name()} last 3 items: "))
            opponent.revert_state(option) # process
            print(f"\nUPDATE: {opponent.get_vibe().capitalize()} {opponent.get_name()} food items and grid positions have been reverted.\n")

            print("AFTER:")
            opponent.display_pocket_content()
            print(f"\n+++ {opponent.get_name().upper()}'S GRID POSITIONS +++")
            print(opponent.get_grid_positions())
            self.remove_food_item(choice)
        # Double Last Food Item
        elif choice == "Double Last Food Item":
            print("BEFORE:")
            player.display_pocket_content()

            player.update_pocket_content(player.get_pocket_content()[-1])
            print(f"\nUPDATE: {player.get_vibe().capitalize()} {player.get_name()} has collected {len(player.get_pocket_content())} food items and has {player.get_pocket_space()} / {Purrson.INITIAL_POCKET_SPACE} pocket space left.\n")
            
            print("AFTER:")
            player.display_pocket_content()
            self.remove_food_item(choice)


######## MAIN GAME FUNCTION #########

def main():
    
    ######## HELPERS ########

    # clears player and position text
    def clear_positions(grid_dictionary: dict) -> None:
        for position in grid_dictionary:
            if "player" in grid_dictionary[position]:
                del grid_dictionary[position]["player"]
            if "position" in grid_dictionary[position]:
                del grid_dictionary[position]["position"]

    def move_turn(purrson: Purrson) -> None:
            print(f"\n{purrson.get_name().upper()}'S TURN...")

            grid_dictionary[purrson.get_current_grid_position()]["player"] = purrson.get_name()
            possible_moves = purrson.get_next_grid_positions(grid_dictionary)
            for move in possible_moves:
                grid_dictionary[move]["position"] = str(move)
            
            display_grid(grid_dictionary)
            clear_positions(grid_dictionary)

            # Prompt to move
            position_option = int(input("\nSelect a grid position to visit next: "))

            if position_option in possible_moves:
                purrson.update_calories_pocket_space(-500, 0)
                print(f"\n{purrson.get_name()} loses 500 calories.")
                purrson.update_grid_position(position_option)
                if purrson.get_vibe() == "neutral":
                    if purrson.get_calories() < 3500:
                        purrson.update_vibe("hangry")
                        print(f"\n{purrson.get_name()} is now {purrson.get_vibe()}.")
                
    def consume_turn(purrson: Purrson) -> None:
        print(f"\n{purrson.get_name().upper()} VISITS...")
        grid_dictionary[purrson.get_current_grid_position()]["player"] = purrson.get_name()
        display_grid(grid_dictionary)
        clear_positions(grid_dictionary)

        if "vibe" in grid_dictionary[purrson.get_current_grid_position()]:
            if ((grid_dictionary[purrson.get_current_grid_position()]["vibe"] == "hangry" and purrson.get_vibe() != "hangry") or 
                        (grid_dictionary[purrson.get_current_grid_position()]["vibe"] == "full" and purrson.get_vibe() != "full")):
                        print(f"\nBLOCKED! Only full purrsons can eat the food in position {purrson.get_current_grid_position()}.\n")
        else:
            # Special food items
            if grid_dictionary[purrson.get_current_grid_position()]["grid object"].get_food_type() == "Special Food":
                opponent = purrson1 if purrson == purrson2 else purrson2
                grid_dictionary[purrson.get_current_grid_position()]["grid object"].select_special_food_item(purrson, opponent)
                
                if purrson.get_vibe() == "hangry":
                    grid_dictionary[purrson.get_current_grid_position()]["vibe"] = "hangry"
                elif purrson.get_vibe() == "full":
                    grid_dictionary[purrson.get_current_grid_position()]["vibe"] = "full"
                
            else:
                grid_dictionary[purrson.get_current_grid_position()]["grid object"].display_food_items(purrson.get_food_dictionary(), purrson.get_pocket_space())

                # Prompt to consume food
                consume_option = input(f"\nSelect a food item to consume (press Enter to select nothing): ")

                # If something is consumed
                if consume_option:
                    
                    # Get food item code
                    consume_option = grid_dictionary[purrson.get_current_grid_position()]["grid object"].get_food_items()[int(consume_option) - 1]

                    # Update grid
                    for position in grid_dictionary:
                        if consume_option in grid_dictionary[position]["grid object"].get_food_items():
                            grid_dictionary[position]["grid object"].remove_food_item(consume_option)
                    if purrson.get_vibe() == "hangry":
                        grid_dictionary[purrson.get_current_grid_position()]["vibe"] = "hangry"
                    elif purrson.get_vibe() == "full":
                        grid_dictionary[purrson.get_current_grid_position()]["vibe"] = "full"

                    # Update purrson
                    purrson.update_calories_pocket_space(round(purrson.get_food_dictionary()[consume_option]["Calories"]), -purrson.get_food_dictionary()[consume_option]["Portion"])
                    purrson.update_pocket_content(consume_option)
                    
                    print(f"\nUPDATE: {purrson.get_name()} has consumed {purrson.get_food_dictionary()[consume_option]['Food Name']} and have {purrson.get_calories()} personal calories.\n")
                    
                    if purrson.get_vibe() == "neutral":
                        if purrson.get_pocket_space() < Purrson.INITIAL_POCKET_SPACE // 2:
                            purrson.update_vibe("full")
                            print(f"{purrson.get_name()} is now {purrson.get_vibe()}.\n")

                    
                    
                else:
                    print(f"UPDATE: {purrson.get_name()} has consumed nothing and have {purrson.get_calories()} personal calories.\n")
        print(purrson)
        purrson.display_pocket_content()

    print("WELCOME TO PURRPETUAL POCKETS!")
    print("Navigate a grid-based world filled with delicious foods!\n")

    print("GAME SETUP...")

    # Food options file
    print("No. File Name")
    food_options_files = ["food_options1.csv", "food_options2.csv", "food_options3.csv", "food_options4.csv"]
    for i, file in enumerate(food_options_files):
        print(f"[{i + 1}] {file}")

    food_options_file = food_options_files[int(input("\nSelect a food option file: ")) - 1]
    ingredients_file = f"ingredients{food_options_file[12]}.csv" # the character at index 12 is the number
    food_dictionary = acquire_food(food_options_file, ingredients_file)
    
    # Initialize grid
    grid_size = int(input("\nSelect a grid size: "))
    grid_dictionary = {i: {} for i in range(1, grid_size ** 2 + 1)}
    for i in grid_dictionary:
        GameGrid(i, grid_dictionary, food_dictionary)
        # Special grid positions
        if grid_dictionary[i]["grid object"].get_food_type() == "No Food Type":
            PurrsperityGrid(i, grid_dictionary, food_dictionary)

    # Purrsons
    purrson1_name = input("\nEnter Purrson 1 name: ")
    purrson1 = Purrson(purrson1_name, acquire_food(food_options_file, ingredients_file))
    purrson2_name = input("\nEnter Purrson 2 name: ")
    purrson2 = Purrson(purrson2_name, acquire_food(food_options_file, ingredients_file))

    # Difficulty level
    difficulty_levels = ["Kitten", "Explorer", "Purrdator"]
    print("\nNo. Difficulty Level")
    for i, level in enumerate(difficulty_levels):
        print(f"[{i + 1}] {level}")

    difficulty_level = difficulty_levels[int(input("\nSelect a difficulty level: ")) - 1]

    if difficulty_level == "Kitten":
        win_conditions = {"Calories": 700, "Carbohydrates": 0, "Fat": 0, "Protein": 0, "Sugars": 0}
    elif difficulty_level == "Explorer":
        totals_dictionary = {"Calories": 0, "Carbohydrates": 0, "Fat": 0, "Protein": 0, "Sugars": 0}
        for food in purrson1.get_food_dictionary():
            for nutrient in totals_dictionary:
                totals_dictionary[nutrient] += purrson1.get_food_dictionary()[food][nutrient]
        win_conditions = {"Calories": round(totals_dictionary["Calories"] / 3), "Carbohydrates": round(totals_dictionary["Carbohydrates"] / 3), "Fat": round(totals_dictionary["Fat"] / 3), "Protein": round(totals_dictionary["Protein"] / 3), "Sugars": round(totals_dictionary["Sugars"] / 3)}
    elif difficulty_level == "Purrdator":
        totals_dictionary = {"Calories": 0, "Carbohydrates": 0, "Fat": 0, "Protein": 0, "Sugars": 0}
        for food in purrson1.get_food_dictionary():
            for nutrient in totals_dictionary:
                totals_dictionary[nutrient] += purrson1.get_food_dictionary()[food][nutrient]
        win_conditions = {"Calories": round(totals_dictionary["Calories"] / 3 * 2), "Carbohydrates": round(totals_dictionary["Carbohydrates"] / 3 * 2), "Fat": round(totals_dictionary["Fat"] / 3 * 2), "Protein": round(totals_dictionary["Protein"] / 3 * 2), "Sugars": round(totals_dictionary["Sugars"] / 3 * 2)}

    purrson1.update_grid_position(1)
    purrson2.update_grid_position(grid_size ** 2)

    
    # Start
    print("\nGAME STARTS...")
    for purrson in [purrson1, purrson2]:
        consume_turn(purrson)

    # Game loop
    is_running = True
    while is_running:
        for purrson in [purrson1, purrson2]:
            move_turn(purrson)
            consume_turn(purrson)

            # Check win conditions
            if purrson.met_win_conditions(win_conditions):
                print(f"\nCONGRATULATIONS! {purrson.get_name()} meets the winning conditions!")
                is_running = False
                break




# if __name__ == "__main__":
#     main()

# TESTING 

from unittest.mock import patch
def custom_input(prompt):
    print(prompt, end='')  # Print the prompt without a newline
    value = input_values_4.pop(0)  # Get the next value from the list
    print(value)  # Print the value
    return value  # Return the value

input_values_1 = ["1", "3", "Doraemon", "Garfield", "1", "1", "2", "2", "3", "8", "2", "1", "1", "9", "", "4", "1"]
input_values_2 = ["1", "3", "Grumpy Cat", "Oyen", "2", "2", "2", "4", "2"]
input_values_3 = ["2", "7", "Crookshanks", "Lucifer", "1", "1", "5", "2", "5", "48", "5", "9", "2", "41", "3", "16", "5"]
input_values_4 = ["2", "5", "Mrs Norris", "Felix", "2", "1", "5", "2", "3", "20", "5", "7", "4", "19", "2", "8", "3", "14", "5", "13", "2", "13", "4", "18", "5", "18", "5", "23", "4", "23", "5", "22", "1", "22", "3", "21", "2", "17", "3", "25", "4", "16", "2", "24", "3", "21", "25", "5"]

if __name__ == "__main__": #do not remove this to avoid failing tests
    with patch("builtins.input", custom_input): 
        main()