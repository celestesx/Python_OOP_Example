import sys

class FrontEnd:
    def __init__(self, backend):
        self.__backend = backend
        self.__backend.load_file()
        
        welcome_message = "\n========================================\n"
        welcome_message += " Welcome to MyFitnessPal Food Tracker\n"
        welcome_message += "========================================\n"
        sys.stdout.write(welcome_message)
        
        menu_choice = FrontEnd.__get_main_menu_choice()
        
        while (menu_choice != 4):
            if (menu_choice == 1):
                sub_menu_choice = FrontEnd.__get_sub_menu_choice()
                while (sub_menu_choice != 6):
                    if (sub_menu_choice == 1):
                        self.__get_food_calories()
                    elif (sub_menu_choice == 2):
                        self.__get_remove_record()
                    elif (sub_menu_choice == 3):
                        self.__display_modify_entry()
                    elif (sub_menu_choice == 4):
                        self.__display_food_calories()
                    elif (sub_menu_choice == 5):
                        self.__display_total_calories()
                    sub_menu_choice = FrontEnd.__get_sub_menu_choice()
            elif (menu_choice == 2):
                self.__display_steps_information()
            elif (menu_choice == 3):
                self.__display_bmi_information()
            menu_choice = FrontEnd.__get_main_menu_choice()
        self.__backend.save_file()
        
        goodbye_text = "\n===============================================\n"
        goodbye_text += "Thank you for using MyFitnessPal Food Tracker!\n"
        goodbye_text += "Until next time! Goodbye.\n"
        sys.stdout.write(goodbye_text)           

    def __get_main_menu_choice():
        menu = "\n============== Main Menu ==============\n"
        menu += "[1] -Food Tracker-                     \n"
        menu += "[2] -Steps / Calories Calculator-      \n"
        menu += "[3] -BMI Calculator-                   \n"
        menu += "[4] -Exit Program-                     \n"
        menu += "=======================================\n\n"
        choice = FrontEnd.__get_int(menu + "Please enter a choice: ")
        
        while (choice > 4) or (choice < 1):
            choice = FrontEnd.__get_int("Please enter a valid choice: ")
        return choice

    def __get_sub_menu_choice():
        sub_menu = "\n=============== Food Tracker ================\n"
        sub_menu += "[1] -Add an Entry-                           \n"
        sub_menu += "[2] -Remove an Entry-                        \n"
        sub_menu += "[3] -Modify an Entry-                        \n"
        sub_menu += "[4] -View Your Entries-                      \n"
        sub_menu += "[5] -View Caloric Consumption Information-   \n"   
        sub_menu += "[6] -Back to Main Menu-                      \n"
        sub_menu += "=============================================\n\n"
        
        choice = FrontEnd.__get_int(sub_menu + "Please enter a choice: ")

        while (choice > 6) or (choice < 0):
            choice = FrontEnd.__get_int("Please enter a valid choice: ")
        return choice
            
    def __get_food_calories(self):
        day = FrontEnd.__get_int("Enter the day: ")
        food = FrontEnd.__get_str("Enter food: ")
        calories = FrontEnd.__get_int("Enter calories: ")      
        self.__backend.add_caloric_intake_record(day, food, calories)
        
    def __get_remove_record(self):
        which_day_remove = "Which day do you want to remove "
        which_day_remove += "your entry from?: "
        day = FrontEnd.__get_int(which_day_remove)
        food = FrontEnd.__get_str("Enter food name: ")
        record_exist = self.__backend.does_record_exist(day, food)

        if (record_exist == True):
            self.__backend.remove_caloric_intake_record(day, food)
            sys.stdout.write("You have removed " + food + " from day " + str(day) + ".\n")
        else:
            sys.stdout.write("That record does not exist.\n")        

    def __display_modify_entry(self):
        which_day_modify = "Which day would you like to modify "
        which_day_modify += "your entry from?: "
        day = FrontEnd.__get_int(which_day_modify)
        old_food = FrontEnd.__get_str("Enter food name: ")
        new_food = FrontEnd.__get_str("What do you want to change it to?: ")
        new_calories = FrontEnd.__get_int("Enter calories: ")
        record_exist = self.__backend.does_record_exist(day, old_food)

        if (record_exist == True):
            try:
                self.__backend.modify_entry(day, old_food, new_food, new_calories)
                changed = "\nYou have changed " + old_food + " to " + new_food
                changed += " in day " + str(day) + ".\n"
                sys.stdout.write(changed)
            except:
                sys.stderr.write("\nThat cannot be done. Please try again.\n")
        else:
            sys.stdout.write("\nThat record does not exist.\n")

     def __display_food_calories(self):
        which_day_entry_text = "Enter the day you "
        which_day_entry_text += "want to view.\n"
        which_day_entry_text += "Your answer:"        
        day_number = FrontEnd.__get_int(which_day_entry_text)        
        food_records_on_day = self.__backend.find_records_on_day(day_number)
        len_food_records_on_day = len(food_records_on_day)

        if (len_food_records_on_day != 0):
            records = ""            
            i = 0
            while (i < len_food_records_on_day):
                records += str(food_records_on_day[i].food).ljust(20)
                records += str(food_records_on_day[i].calories) + "\n"
                i += 1

            entries_heading = "\nOn day " + str(day_number)
            entries_heading += ", you have consumed the "
            entries_heading += "following:\n"
            entries_heading += "================================"
            entries_heading += "=============\n"
            entries_heading += "FOOD".ljust(20)
            entries_heading += "CALORIES \n"
            entries_heading += "================================"
            entries_heading += "=============\n"
            sys.stdout.write(entries_heading)
            sys.stdout.write(records)
        else:
            sys.stdout.write("No records for that day.\n")

    def __display_total_calories(self):
        target_calories_text = "Please enter target calories: "
        specify_calories = FrontEnd.__get_int(target_calories_text)
        which_day_calories_text = "Enter the day you "
        which_day_calories_text += "want to calculate.\n"
        which_day_calories_text += "Your answer: "
        day_number = FrontEnd.__get_int(which_day_calories_text)
        total_calories = self.__backend.calculate_total_calories(day_number)

        if (total_calories != 0):
            calories_percent = (total_calories/specify_calories)*100
            calories_information = "\nYou have consumed "
            calories_information += str(total_calories)
            calories_information += " calories on day " + str(day_number)
            calories_information += ".\nThis amounts to "
            calories_information += f"{calories_percent:.2f}"
            calories_information += "% of your target caloric intake of "
            calories_information += str(specify_calories) + ".\n"
            
            sys.stdout.write(calories_information)
        else:
            sys.stdout.write("No calories were consumed that day.\n")

    def __display_steps_information(self):
        steps_question = "Enter your steps today: "
        steps = FrontEnd.__get_int(steps_question)
        
        try:
            calories_burned_value = self.__backend.calculate_steps(steps)
            calories_burned_conclusion = "\n================================="
            calories_burned_conclusion += "===========\n\n"
            calories_burned_conclusion += "--You walked " + str(steps)
            calories_burned_conclusion += " steps today.\n"
            calories_burned_conclusion += "--You have burned approximately "
            calories_burned_conclusion += f"{calories_burned_value:.2f}"
            calories_burned_conclusion += " calories.\n\n"
            calories_burned_conclusion += "=================================="
            calories_burned_conclusion += "=============\n"
            calories_burned_conclusion += "--This calculation is based on the "
            calories_burned_conclusion += "average person\n"
            calories_burned_conclusion += "weighing 70kg and is 183cm tall, "
            calories_burned_conclusion += "walking at a\n"
            calories_burned_conclusion += "speed of 4.8km/h which is an "
            calories_burned_conclusion += "average pace.\n"
            calories_burned_conclusion += "=================================="
            calories_burned_conclusion += "=============\n"
            sys.stdout.write(calories_burned_conclusion)
        except:
            sys.stderr.write("No calories will be burned without steps.\n")

    def __display_bmi_information(self):
        question_meters = "Enter your height in meters(m) : "
        question_kg = "Enter your weight in kilograms(kg) : "
        height = FrontEnd.__get_float(question_meters)
        weight = FrontEnd.__get_int(question_kg)

        try:
            bmi_value = self.__backend.calculate_bmi(weight, height)
            bmi_conclusion = "\nYour BMI is " + f"{bmi_value:.2f}" + ". "
            bmi_conclusion += self.__backend.bmi_status(bmi_value) + "\n"        
            sys.stdout.write(bmi_conclusion)
        except:
            sys.stderr.write("Neither values can be 0.\n")

    def __get_str(prompt:str) -> str:
        sys.stdout.write(prompt)        
        sys.stdout.flush()
        string = sys.stdin.readline().strip()
        while (string == ""):
            sys.stdout.write("Input cannot be blank.Re-enter: ")
            sys.stdout.flush()
            string = sys.stdin.readline().strip()
        return string

    def __get_float(prompt:str) -> float:
        problem_with_input = True
        while problem_with_input:
            try:
                float_num = float(FrontEnd.__get_str(prompt))
                problem_with_input = False
            except ValueError:
                sys.stderr.write("That wasn't right. Enter a float. \n")
                prompt = "Please enter a choice: "
        return float_num

    def __get_int(prompt:str) -> int:
        problem_with_input = True
        while problem_with_input:
            try:
                integer = int(FrontEnd.__get_str(prompt))
                problem_with_input = False
            except ValueError:
                sys.stderr.write("That wasn't right. Enter an integer. \n")
                prompt = "Please enter a choice: "
        return integer
