import sys

#justify the code block
#----------------------
#class FrontEnd was created to contain the main user interface function of the
#MyFitnessPal program. It contains the necessary methods to enable to program
#to operate as intended. Alternatively, object-oriented programming need not be
#used but for the purpose of this assessment, using classes, objects and methods
#are the most suitable.
class FrontEnd:
    #justify the code block
    #----------------------
    #This method is the class constructor which is used to initialize the
    #instance of the class FrontEnd. The arguments used are self, and backend.
    #self refers to the a specific instance of an object. The second argument,
    #backend, is used to call the backend when imported to application.py.
    #Alternatively, if application.py was not used, a class constructor also
    #need not be used. Instead, a function called main could be used and called.
    def __init__(self, backend):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. self.__backend
        #self.__backend was used as the name for this variable as it makes it
        #private. Alternatively, back_end could be used. The type that is held
        #in this variable is the instruction to call the class 'BackEnd'.
        #There is no close alternative to this.
        #2. welcome_message
        #welcome_message was used as the name for this variable as it contained
        #the first message that is displayed to the user when the program is
        #open. Alternatively, welcome could be used as a name. The data type is
        #string as it contained alphabets. There is no alternative data type
        #for the function it needs to perform.
        self.__backend = backend
        self.__backend.load_file()
        
        welcome_message = "\n========================================\n"
        welcome_message += " Welcome to MyFitnessPal Food Tracker\n"
        welcome_message += "========================================\n"
        sys.stdout.write(welcome_message)
        
        #justify the variable and datatype
        #---------------------------------
        #menu_choice was used as the name for this variable as it contains the
        #choice entered by the user through the function that is called. Other
        #names are user_choice of user_menu_choice. The datatype is integer
        #as the menu choices asked for the user to enter numbers. Alternatively,
        #string type could be used if the choices were in alphabets and did not
        #require shorter comparison operators and code blocks used.
        menu_choice = FrontEnd.__get_main_menu_choice()
        
        #justify the code block
        #----------------------
        #A while statement is used to force repetition of the main menu to
        #display until the user has entered 4 which is to exit the program.
        #A close alternative would be to use generators which act like
        #functions and yield values which can be used in a for loop.
        #However, this method would fall out of scope of this assignment.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used is a comparison operator as it needed to check if
        #the user has entered 4 which is to exit the program. Alternatively,
        #it can be written in a much longer was such as menu_choice == 1 or
        #menu_choice == 2 or menu_choice == 3. An identity operator such as
        #'is not' could be used.
        while (menu_choice != 4):
            #justify the code block
            #----------------------
            #If, elif statements are used to check if the user has entered the
            #right input for the part of the program they wish to acesses. This
            #will activate the part of the program to function. There is no
            #close alternative for the functions the program needs.
            #----------------------
            #justify the condition
            #----------------------
            #Comparison operators are used. Alternatively, identity operators
            #could be used.
            if (menu_choice == 1):
                #justify the variable name and its data type
                #-------------------------------------------
                #sub_menu_choice is used for the name of this variable as it
                #contains choice entered by the user through the function that
                #is called. Other names could be sub_menu_user_choice or
                #sub_menu_answer. The datatype is integer as the user is asked
                #to enter a number from the sub menu. Alternatively, string type
                #could be used if the user was asked to enter alphabets as
                #choices.
                sub_menu_choice = FrontEnd.__get_sub_menu_choice()
                #justify the code block
                #----------------------
                #A while statement is used to force repetition of the sub menu
                #to display until the user wishes to get out of the sub menu and
                #go back to main menu. A close alternative would be using a for
                #loop iterating over a generator. 
                #----------------------
                #justify the condition
                #----------------------
                #The condition used is a comparison operator as it needed to
                #check if the user has entered 4 which is to exit the program.
                #Alternatively, it can be written in a much longer was such as
                #sub_menu_choice == 1 or menu_choice == 2 or menu_choice == 3 or
                #sub_menu_choice == 4. An identity operator such as 'is not'
                #could be used.
                while (sub_menu_choice != 6):
                    #justify the code block
                    #----------------------
                    #if and elif statements are used to check if the user has
                    #entered the sub menu options which will activate a part of
                    #the program to function. There is no close alternative
                    #for the functions the program needs.
                    #----------------------
                    #justify the condition
                    #----------------------
                    #Comparison operators were used for these if elif
                    #statements. Alternatively, an identity operator "is" could
                    #be used.
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
        
        #justify the variable and datatype
        #---------------------------------
        #goodbye_text is used as the name of this variable as it contains the
        #sentence that displays to the user as they exit the program. Other
        #names could be goodbye or final_text. The datatype is string as this
        #is a string concatenation. There is no close alternative data type
        #for this purpose.
        goodbye_text = "\n===============================================\n"
        goodbye_text += "Thank you for using MyFitnessPal Food Tracker!\n"
        goodbye_text += "Until next time! Goodbye.\n"
        sys.stdout.write(goodbye_text)           

    #justify the code block
    #----------------------
    #This static method contains the code that displays the main menu and
    #solicits a choice from the user from the menu items. It takes no
    #parameters therefore is a static method. This menu appears many times in
    #the course of this program that is why it is in a method to be called
    #when needed. Alternatively, this can be included in the constructor of the
    #class.
    def __get_main_menu_choice():
        #justify the variable name and its data type
        #-------------------------------------------
        #menu was used as the name for this variable as it contains the menu of
        #the program. Alternatively, main_menu could be used but menu was
        #sufficiently descriptive. The datatype is string as it contained the
        #menu which is made of alphabetical characters. There is no close
        #alternative for the purpose it needs to perform.
        menu = "\n============== Main Menu ==============\n"
        menu += "[1] -Food Tracker-                     \n"
        menu += "[2] -Steps / Calories Calculator-      \n"
        menu += "[3] -BMI Calculator-                   \n"
        menu += "[4] -Exit Program-                     \n"
        menu += "=======================================\n\n"
        #justify the variable and datatype
        #---------------------------------
        #choice is the name for this variable as it needs to be stored when
        #retrieved from the user. Other variable names chould be user_input or
        #user_choice. The datatype is int as the value stored will be used in
        #a > and < comparison operator. Alternatively, string datatype could be
        #used. 
        choice = FrontEnd.__get_int(menu + "Please enter a choice: ")
        #justify the code block
        #----------------------
        #A while statement is used to validate the user input. Alternatively,
        #if and else statements could be used but will not be able to repeatedly
        #ask the user to return a valid response.
        #----------------------
        #justify the condition
        #----------------------
        #The conditionals used are comparison and logical operators. They
        #can be written in an opposite way to achieve the same results.        
        while (choice > 4) or (choice < 1):
            choice = FrontEnd.__get_int("Please enter a valid choice: ")
        return choice

    #justify the code block
    #----------------------
    #This static method contains the code that displays the sub menu and
    #solicits a choice from the user from the menu items. It takes no
    #parameters therefore is a static method. This sub menu appears many times
    #in the course of this program that is why it is in a method to be called
    #when needed. Alternatively, the same functions could be achieved by putting
    #this in the constructor.
    def __get_sub_menu_choice():
        #justify the variable and datatype
        #---------------------------------
        #sub_menu was the name for this variable as it contained
        #the sub menu texts that outputs to the user. Alternatively, submenu
        #could be used. The datatype is string as it contains the sub menu to be
        #displayed to the user. There is no close alternative for the purposes
        #it is intended to perform.
        sub_menu = "\n=============== Food Tracker ================\n"
        sub_menu += "[1] -Add an Entry-                           \n"
        sub_menu += "[2] -Remove an Entry-                        \n"
        sub_menu += "[3] -Modify an Entry-                        \n"
        sub_menu += "[4] -View Your Entries-                      \n"
        sub_menu += "[5] -View Caloric Consumption Information-   \n"   
        sub_menu += "[6] -Back to Main Menu-                      \n"
        sub_menu += "=============================================\n\n"
        
        choice = FrontEnd.__get_int(sub_menu + "Please enter a choice: ")

        #justify the code block
        #----------------------
        #While statement is used to force repetition so that the user is able
        #to enter the right choice to proceed with the program. Alternatively,
        #complicated if, elif and else statements could be used. However, that
        #method will not allow repetition to enter the valid response needed.
        #----------------------
        #justify the condition
        #----------------------
        #The conditions use are comparison and logical operators. Alternatively,
        #this could be written in an opposite way.
        while (choice > 6) or (choice < 0):
            choice = FrontEnd.__get_int("Please enter a valid choice: ")
        return choice
            
    #justify the code block
    #----------------------
    #This class method is used as data input retrieval to get the day, food and
    #calories variables from the user. It will then be used to call a method
    #from the backend to append to a list of instances. Alternatively, this
    #could exist in the constructor.
    def __get_food_calories(self):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. day
        #day is used as the variable name as it contains
        #the day the user enters when prompted. Other names are
        #day_entry or day_data.The datatype is
        #integer for the reasons stated above.
        #2. food
        #food is the name chosen for this variable as it
        #contains the food names the user wishes to enter when
        #prompted. Other names could be food_name or food_entry.
        #The datatype is string for the reasons stated above.
        #3. calories_choice
        #calories is the name chosen for this variable as it
        #contains the caloric details of the food the user had
        #entered. Other names could be caloric_detail or
        #calories_info. The datatype is integer for the reasons
        #stated above.
        day = FrontEnd.__get_int("Enter the day: ")
        food = FrontEnd.__get_str("Enter food: ")
        calories = FrontEnd.__get_int("Enter calories: ")      
        self.__backend.add_caloric_intake_record(day, food, calories)
        
    #justify the code block
    #----------------------
    #This class method is used to retrieve the data input by the user for the
    #purpose of removing records. The data collected will be used to call a
    #method from the backend to remove selected records. Alternatively, this
    #could be written in the constructor. 
    def __get_remove_record(self):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. which_day_remove
        #which_day_remove is used as the variable name as it contains the
        #questions that solicits an answer from the user of which day the user
        #wishes to access to remove records. Other names could be
        #remove_day_text. The datatype is string as it contains a query.
        #2. day
        #day was used as the name for this variable because it contains the
        #answer which is entered by the user of which day to access. Other names
        #could be target_day or search_day. The datatype is integer as the days
        #are in numbers.
        #3. food
        #food is used as the variable name as it contains the names of the food
        #that the user wants to removed when retrieved from the user. Other
        #names include search_food or target_food. The datatype is string as it
        #contains the names of the food.
        #4. record_exist
        #record_exist was used as the name of this variable as it takes the
        #input by the user to use a backend method to check if a certain record
        #the user wishes to remove, exists. The data type is boolean as it
        #represents the state of whether the record exists or not. Alternatively
        #strings "yes" or "no" could be used.
        which_day_remove = "Which day do you want to remove "
        which_day_remove += "your entry from?: "
        day = FrontEnd.__get_int(which_day_remove)
        food = FrontEnd.__get_str("Enter food name: ")
        record_exist = self.__backend.does_record_exist(day, food)

        #justify the code block
        #----------------------
        #if and else statement is used to check if the backend has returned a
        #"True" value. If it doesn then the record selected by the user will be
        #removed via another backend method. If backend has returned a "False"
        #value, then the user will be informed that the record does not exist.
        #Alternatively, try and except could be used.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used is a comparison operator. Alternatively, identity
        #operatos "is" could be used. 
        if (record_exist == True):
            self.__backend.remove_caloric_intake_record(day, food)
            sys.stdout.write("You have removed " + food + " from day " + str(day) + ".\n")
        else:
            sys.stdout.write("That record does not exist.\n")        

    #justify the code block
    #----------------------
    #This class method was used to to get the entries the user wants to modify.
    #It will call on the back end method perform the iteration to look for the
    #the entry the user needs to change and then once found will change it into
    #what the user defines as the new entry. Alternatively, we need not have
    #this method, but to ask the user to remove entries and add new ones
    #instead.
    def __display_modify_entry(self):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. which_day_modify
        #which_day_modify is used to store the string which contains the
        #question which asks the user from which day the record needs to be
        #changed. Other names include which_day or day_to_modify_question.
        #The data type is string as it contains letters and words to be displayed
        #to the user. There is no close alternative for the data type.
        #2. old_food
        #old_food is a variable that stores the food name the user needs to
        #change or modify. Other names include food_to_change or old_food_name.
        #The data type is string as the input required is used to search for the
        #exact names in the records list. There is no alternative for its
        #intended purposes.
        #3. new_food
        #new_food is a variable that stores the food name the user needs to
        #change old_food to. Other names are change_food_name or new_food_name.
        #The data type is string as food names often are composed with alphabets.
        #There is no close alternative for its intended purposes.
        #4. new_calories
        #new_calories was selected as the name for this variable as when the user
        #enters a new food, they must enter a calories value that corresponds to
        #the food they have entered. Other names include, new_food_calories, and
        #changed_food_calories. The datatype is integer as calories are usually
        #defined in whole numbers. Alternatively, float could be used but most
        #users are not able to discern calories to the decimal.
        #5. record_exist
        #record_exist was used as the name of this variable as it takes the
        #input by the user to use a backend method to check if a certain record
        #the user wishes to remove, exists. The data type is boolean as it
        #represents the state of whether the record exists or not. Alternatively
        #strings "yes" or "no" could be used.
        which_day_modify = "Which day would you like to modify "
        which_day_modify += "your entry from?: "
        day = FrontEnd.__get_int(which_day_modify)
        old_food = FrontEnd.__get_str("Enter food name: ")
        new_food = FrontEnd.__get_str("What do you want to change it to?: ")
        new_calories = FrontEnd.__get_int("Enter calories: ")
        record_exist = self.__backend.does_record_exist(day, old_food)

        #justify the code block
        #----------------------
        #An if statement was used to check if the old_food entered exists in the
        #list of records. If it was true, the following code will be executed.
        #Alternatively, a while loop could be used to enable the user to
        #repeatedly input if the record does not exist. However, the user may
        #not remember exactly what they entered and it would cause issues with
        #the program if the user can not enter a correct input. Therefore, an
        #if else statement seems to be the best choice for this program.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used is a comparison operator which checks if the the
        #value stored in record_exist was True or False. Alternatively, an "is"
        #identity operator could be used in this scenario.
        if (record_exist == True):
            #justify the code block
            #----------------------
            #A try and except statement was used to validate the user inputs. In
            #event a ValueError had occured, it will be displayed to the user
            #that they could not change the record. Alternatively, this would
            #not be needed if the exception is handled elsewhere.
            try:
                self.__backend.modify_entry(day, old_food, new_food, new_calories)
                #justify the variable name and its data type
                #-------------------------------------------
                #changed stores the string that displays to the user what the
                #user needed to change and the alterations. Other names are
                #food_change or changed_information_text. The data type is
                #string as it contains a message made of alphabets and words.
                #There is no alternative for the purpose it needs to perform.
                changed = "\nYou have changed " + old_food + " to " + new_food
                changed += " in day " + str(day) + ".\n"
                sys.stdout.write(changed)
            except:
                sys.stderr.write("\nThat cannot be done. Please try again.\n")
        else:
            sys.stdout.write("\nThat record does not exist.\n")

        
    #justify the code block
    #----------------------
    #This class method is used to retrieve the day's data and using it as a
    #parameter in a backend method to find the records corresponding the the
    #day the user has input. Alternatively, this can be written in the elif
    #statement in the constructor.
    def __display_food_calories(self):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. which_day_entry_text
        #which_day_entry_text was used as the name for this variable as it
        #contains the questions that is asked to the user on which day the user
        #wishes to view. Other names are which_day or choose_day. The datatype
        #is string as it contains the question that is asked to the user.
        #2. day_number
        #day_number is used as the name for this variable as it contains the
        #choice of day that is retrieved from the user when prompted. The
        #datatype is integer for the reasons stated above.
        #3. food_records_on_day
        #food_records_on_day is used as the the name for this variable as it
        #calls a backend method to return a list of foods recorded on the day
        #the user has chosen. The data type is list. Alternatively, string
        #could be used but it will require the backend to handle it which is
        #undesirable.
        #4. len_food_records_on_day
        #len_food_records_on_day is used as the name for this variable as it
        #contains the integer which is the length of the list that was returned.
        #Other names could be length_list or lenght_of_returned_list.
        #Alternatively, this can be omitted and len(len_food_records_on_day)
        #can be used in the condition for the following if statement.
        which_day_entry_text = "Enter the day you "
        which_day_entry_text += "want to view.\n"
        which_day_entry_text += "Your answer:"        
        day_number = FrontEnd.__get_int(which_day_entry_text)        
        food_records_on_day = self.__backend.find_records_on_day(day_number)
        len_food_records_on_day = len(food_records_on_day)

        #justify the code block
        #----------------------
        #If and else statements are used to check if there were any records
        #entered for that day. If records exist, they will be converted to
        #strings and concatenated to be displayed to the user. If not, a
        #message will be displayed to the user to inform them that no records
        #exist on that day that they have chosen. Alternatively,
        #try and except statements could be used.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used is a comparison operator. It can be written in an
        #alternative way such as using 'len_food_records_on_day > 0'. 
        if (len_food_records_on_day != 0):
            #justify the variable name and its data type
            #-------------------------------------------
            #1.records
            #records was used as the name for this variable as it will contain
            #the concatenation of strings that will be addedd to it as the list
            #of found records was iterated. Alternatively, data or items could
            #be used. The data type is string as it contains texts to be
            #displayed to the user. There is no close alternative for the
            #purpose it needs to perform.
            #2. i
            #i was used as the variable name as it is representing an index
            #number. Alternatively, index or index_num could be used. The data
            #type is integer. There is no alternative for this since this is
            #used as an index number.
            records = ""            
            i = 0
            #justify the code block
            #----------------------
            #A while loop is used to iterate through the food_records_on_day
            #list that was generated. Alternatively, a for loop could be used.
            #----------------------
            #justify the condition
            #----------------------
            #A comparison operator was used to stop the loop if the index was
            #larger than the length of the generated list. Alternatively, it
            #can be written in an opposite way.
            while (i < len_food_records_on_day):
                records += str(food_records_on_day[i].food).ljust(20)
                records += str(food_records_on_day[i].calories) + "\n"
                i += 1

            #justify the variable name and its data type
            #-------------------------------------------
            #entries_heading is used as the name for this variable as it
            #contained the heading text of the data that will display
            #after it. Other names could be heading or title. The data
            #type is string as the data it holds contain alphabets to be
            #displayed.
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


    #justify the code block
    #----------------------
    #This class method is created for the purpose of retrieving the day the
    #user wants to display the total calories they have consumed. It will then
    #call a method from backend to calculate a total and be returned to be
    #displayed to the user. Alternatively, this code below it could be written
    #in the constructor. 
    def __display_total_calories(self):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. target_calories_text is used as the name for this variable as it
        #contains the question that asks the user to enter their target caloric
        #intake for a specific day. Other names are target_calories_question.
        #The datatype is string as it contains alphabets to be displayed.
        #2. specify_calories
        #specify_calories is used as it stores the value entered by the user
        #when it is retrieved. Other names are calories_choice or
        #target_calories. The datatype is integer as arithmetic needs to be
        #used on the variable.
        #3. which_day_calories_text
        #which_day_calories_text is used as the name for this variable as it
        #asks the user to enter the day the user wishes to calculate total
        #calories againsts target calories. Other name could have been
        #which_day. The data type is string as it contains a question to be
        #displayed.
        #4. day_number
        #day_number is used as the name for this variable as it contains the
        #choice of day that is retrieved from the user when prompted. The
        #datatype is integer for the reasons stated above.
        #5. total_calories
        #total_calories is used as the name for this variable as it contains the
        #total calories calculated in the backend for a specific day the user
        #entered. Alternative names for this is totalcalories or total_cal.
        #The data type is integer. Alternatively, it could be a float data
        #type.
        target_calories_text = "Please enter target calories: "
        specify_calories = FrontEnd.__get_int(target_calories_text)
        which_day_calories_text = "Enter the day you "
        which_day_calories_text += "want to calculate.\n"
        which_day_calories_text += "Your answer: "
        day_number = FrontEnd.__get_int(which_day_calories_text)
        total_calories = self.__backend.calculate_total_calories(day_number)

        #justify the code block
        #----------------------
        #If and else statements were used to check if any calories were consumed
        #in the day the user has chosen. This is to improve user experience.
        #If calories were not consumed on that day it will simply inform the
        #the user that they had not added any records that day thus no calories
        #were consumed. Alternatively, try and except could be used.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used was a comparison operator. Alternatively, identity
        #operators is not or another comparison operator ">" could be used.
        if (total_calories != 0):
            #justify the variable name and its data type
            #-------------------------------------------
            #1. calories_percent
            #calories_percent is used as a name for this variable as it
            #is the returned value when calculated in another function.
            #An alternative could be cals_percent. The data type is
            #float. Integer datatypes could not be used as the
            #calculations are bound to return a figure with decimals.
            #2. calories_information
            #calories_information was used as the name for this variable
            #as it contains the text that represents the information the
            #user has asked for. Alternative names could be cals_info
            #or caloric_info. The datatype is string as it contains
            #sentences made of words for this string concatenation.
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

    #justify the code block
    #----------------------
    #This class method was created to retrieve the number of steps done by the
    #user. It will then call a backend method to calculate the number of
    #calories burned by the user as a result of taking those steps.
    #Alternatively, this could be a static method with the calculations done
    #on the front end as it does not use any information contained in the
    #backend.
    def __display_steps_information(self):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. steps_question
        #This variable was used because it contained the question that is
        #asked to the user about the amount of steps the user has taken.
        #Another name could be enter_steps_question. The dataype is string
        #as it contains a question.
        #2. steps
        #steps is used as the variable name as it contains the user
        #response when queried. Alternatively, steps_amount could be used.
        #The datatype is integer as the number of steps are usually whole
        #numbers.
        steps_question = "Enter your steps today: "
        steps = FrontEnd.__get_int(steps_question)
        
        #justify the code block
        #----------------------
        #Try and except was used to check if the user has entered 0 as it will
        #cause a ZeroDivisionError to be raised in the backend. If the user had
        #entered 0, then an error message will be displayed to the user.
        #Alternatively, if else could be used.
        try:
            #justify the variable name and its data type
            #-------------------------------------------
            #1. calories_burned_value
            #This variable name was used to store the value that is returned
            #from a method that calculates the calories burned value. Another
            #name for this variable could be calories_burned. The datatype is
            #float as it contains numbers with decimal point.
            #2. calories_burned_conclusion
            #calories_burned_conclusion is used as the name for this string
            #concatenation. Another name could be cals_burned_info. The
            #datatype is string as it contains sentences.
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

    #justify the code block
    #----------------------
    #This class method was created to retrieve the user's height and weight
    #and using a backend method, to calculate the BMI of the user and displaying
    #the BMI range. Alternatively, this could be a static method or even a
    #function if the calculations were to be performed in the front end.
    def __display_bmi_information(self):
        #justify the variable name and its data type
        #-------------------------------------------
        #1. question_meters, question_kg
        #question_meters and question_kg was used to display the questions
        #to be asked to the user about their height and weight for the
        #purpose of calculating their BMI. Other names could be q1 and q2.
        #These contain string datatypes as it contains sentences.
        #2. height, weight
        #height and weight was used as the names of these variables as they
        #store the values of height and weight when retrieved from the user.
        #Other names could be meters and kilograms. The datatypes are float
        #and integer. Alternatively, they could both be float datatypes.
        question_meters = "Enter your height in meters(m) : "
        question_kg = "Enter your weight in kilograms(kg) : "
        height = FrontEnd.__get_float(question_meters)
        weight = FrontEnd.__get_int(question_kg)

        #justify the code block
        #----------------------
        #Try and except was used to check if the user has entered 0 as it will
        #cause a ZeroDivisionError to be raised in the backend. If the user had
        #entered 0, then an error message will be displayed to the user.
        #Alternatively, if else could be used.
        try:
            #justify the variable name and its data type
            #-------------------------------------------
            #1. bmi_value
            #bmi_value was used as a name because it contains the returned
            #value calculated in another function. Other names could be
            #bmi_number or bmi. The datatype is float as it contains decimal
            #values.
            #2. bmi_conclusion
            #bmi_conclusion is the name used for the variable that stores the
            #text that displays to the user about their bmi status. An
            #alternative name could be bmi_info. The datatype is string as this
            #is a concatenation of sentences.
            bmi_value = self.__backend.calculate_bmi(weight, height)
            bmi_conclusion = "\nYour BMI is " + f"{bmi_value:.2f}" + ". "
            bmi_conclusion += self.__backend.bmi_status(bmi_value) + "\n"        
            sys.stdout.write(bmi_conclusion)
        except:
            sys.stderr.write("Neither values can be 0.\n")

    #justify the code block
    #----------------------
    #This function contains the code block that validates the user input as string.
    #The reason this is in a def statement is because it is used throughout the
    #program to solicit the right answer to enable the program to work as intended.
    #The parameters of this function is a prompt which is of a string datatype.
    #It will return a string value at the end of this function. The reason for this
    #is a string answer needed to be obtained from the user. 
    def __get_str(prompt:str) -> str:
        sys.stdout.write(prompt)        
        sys.stdout.flush()
        #justify the variable name and its data type
        #-------------------------------------------
        #string is used as the name for this variable as the program is requiring
        #an input of a string type from the user when queried. Alternatively,
        #value could be used but it is not as descriptive as 'string'.
        string = sys.stdin.readline().strip()
        #justify the code block
        #----------------------
        #A while statement is used to force repetition if the user does not enter
        #anything. This is to solicit an answer of a string datatype from the user.
        #Alternatively, try and except statements could be used.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used here is a comparison operator where if the string was
        #empty, the loop will continue. Alternatively, an
        #identity operator could be used.
        while (string == ""):
            sys.stdout.write("Input cannot be blank.Re-enter: ")
            sys.stdout.flush()
            string = sys.stdin.readline().strip()
        return string

    #justify the code block
    #----------------------
    #This function contains the code block that validates the input as a float
    #value. The reason this is in a def statement is because it is used throughout
    #the program to solicit the right answer to enable the program to work as
    #intended. The parameters of this function is a prompt which is of a string
    #datatype and calling this function will return a float datatype.
    def __get_float(prompt:str) -> float:
        #justify the variable name and its data type
        #-------------------------------------------
        #problem_with_input was used as the name for this variable as it is used
        #to represent if the user input is a float or not. This variable is used
        #to exit out of the loop. Alternatively, input_issue could be used. The
        #data type is boolean. Alternatively, any integer or string could be used,
        #but those will not represent what the function is trying to execute.
        problem_with_input = True
        #justify the code block
        #----------------------
        #A while statement is used to force repetion to solicit the right input
        #from the user. Alternatively, if and else statements could be used.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used for this while loop is if problem_with_input = True.
        #Alternatively, a comparison statement could be used.
        while problem_with_input:
            #justify the code block
            #----------------------
            #Try and except was used to handle a ValueError which will be caused
            #by the user if they input something like a string. Alternatively,
            #if else with conditions could be used to force the user to enter the
            #right inputs.
            try:
                #justify the variable name and its data type
                #-------------------------------------------
                #float_num was used as the variable name as it contains the float
                #the user will input following a query. Another name could have
                #been float but that is syntax function. Therefore, float_num
                #was used. The data type is float as it contains a float value.
                #An alternative datatype could be integer but float is more
                #suitable for the purpose of this program.
                float_num = float(FrontEnd.__get_str(prompt))
                problem_with_input = False
            except ValueError:
                sys.stderr.write("That wasn't right. Enter a float. \n")
                #justify the variable name and its data type
                #-------------------------------------------
                #prompt was used as the name for this variable as it is meant to
                #output to the user to instruct them of the actions needed to be
                #completed. This is also a parameter in this function.
                #Alternatively, question could be used. The data type is string as
                #it does and will hold string values. There is no close alternative
                #data type for the purpose it needs to perform.
                prompt = "Please enter a choice: "
        return float_num

    #justify the code block
    #----------------------
    #This function contains the code block that validates the input as integer
    #datatype. The reason this is in a def statement is because it is used
    #throughout the program to solicit the right answer to enable the program to
    #work as intended. The parameters of this function is a prompt which is of a
    #string datatype. It will return an integer value at the end of this function.
    #The reason for this is an integer answer needed to be obtained from the user.
    def __get_int(prompt:str) -> int:
        #justify the variable name and its data type
        #-------------------------------------------
        #problem_with_input is the name of the variable used to stop the while
        #loop. Alternatively, a nondescript name such as problem or i could be
        #used but this was used as it was more descriptive in its purpose. It
        #holds a boolean datatype. Another datatype such as integer could be used.
        problem_with_input = True
        #justify the code block
        #----------------------
        #A while statement is used to force repetition if the user does not enter
        #an integer. This is to solicit the right answer to enable the program
        #to work correctly. Alternatively, an if, elif statement could be used.
        #----------------------
        #justify the condition
        #----------------------
        #The condition used here is if problem_with_input is True. Alternatively,
        #a comparison operator == could be used.
        while problem_with_input:
            #justify the code block
            #----------------------
            #Try and except was used to handle a ValueError which will be caused
            #by the user if they input something like a string. Alternatively,
            #if else with conditions could be used to force the user to enter the
            #right inputs.
            try:
                #justify the variable name and its data type
                #-------------------------------------------
                #integer is used as the name of this variable because it holds
                #an integer value when retrieved from the user. Alternatively, int
                #could be used. There are no close alternatives for the data type
                #it needs for the purpose of this program.
                integer = int(FrontEnd.__get_str(prompt))
                problem_with_input = False
            except ValueError:
                sys.stderr.write("That wasn't right. Enter an integer. \n")
                prompt = "Please enter a choice: "
        return integer
