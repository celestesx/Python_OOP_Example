class CaloricIntakeRecord:
    __day = 0
    __food = ""
    __calories = 0
    
    def __init__(self, day:int, food:str, calories:int):
        self.__day = day
        self.food = food
        self.calories = calories

    @property
    def day(self): 
        return self.__day

    @property
    def food(self): 
        return self.__food

    @property
    def calories(self):
        return self.__calories

    @food.setter
    def food(self, value:str):
        if (value != "") or (len(value) > 2) or (value != None):
            self.__food = value
        else:
            raise ValueError("Invalid food!")

    @calories.setter
    def calories(self, value:int):
        if (value > 1):
            self.__calories = value
        else:
            raise ValueError("Invalid calories!")

class BackEnd:
    def __init__(self, file_name:str):
        self.__file = file_name
        self.__food_calories = []

    def load_file(self) -> str:
        try:
            input_file = open(self.__file, "r")
            line = input_file.readline()
            while(line != ""):
                fields = line.strip().split(",")
                day_from_csv = int(fields[0])
                food_from_csv = fields[1]
                calories_from_csv = int(fields[2])
                self.add_caloric_intake_record(day_from_csv, food_from_csv, calories_from_csv)
                line = input_file.readline()
            input_file.close()              
        except FileNotFoundError:
            create_file = open(self.__file, "x")
            create_file.close()            
        self.__has_unsaved_changes = False

    def save_file(self):
        if (self.__has_unsaved_changes == True):
            lines_to_write = ""
            len_food_calories = len(self.__food_calories)
            i = 0         
            while (i < len_food_calories):               
                line = str(self.__food_calories[i].day) + ","
                line += self.__food_calories[i].food + ","
                line += str(self.__food_calories[i].calories) + "\n"
                lines_to_write += line
                i += 1       
            output_file = open(self.__file, "w")
            output_file.write(lines_to_write)
            output_file.close()

    def add_caloric_intake_record(self, day:int, food:str, calories:int):
        self.__food_calories.append( CaloricIntakeRecord(day, food, calories) )
        self.__has_unsaved_changes = True
        
    def does_record_exist(self, day:int, food:str) -> bool:
        record_exist = False
        i = 0
        len_food_calories = len(self.__food_calories)
        while (i < len_food_calories):
            if (self.__food_calories[i].day == day) and (self.__food_calories[i].food == food):
                record_exist = True 
            i += 1              
        return record_exist
            
    def remove_caloric_intake_record(self, day:int, food:str):
        records_to_del = []
        len_food_calories = len(self.__food_calories)
        search_target_day = day
        search_target_food = food           
        i = 0
        while (len_food_calories > i):
            if (search_target_day == self.__food_calories[i].day and search_target_food == self.__food_calories[i].food):
                records_to_del.append(self.__food_calories[i])
            i += 1

        j = 0
        while(len(records_to_del) > j):            
            self.__food_calories.remove(records_to_del[j])
            j += 1                
        self.__has_unsaved_changes = True

    def modify_entry(self, day:int, old_food:str, new_food:str, new_calories:int):
        len_food_calories = len(self.__food_calories)
        matches = 0
        i = 0       
        while(i < len_food_calories and matches < 2):
            matches = 0
            if (self.__food_calories[i].day == day):
                matches += 1
            if (self.__food_calories[i].food == old_food):
                matches += 1
            if (matches < 2):
                i += 1
        if (matches >= 2):
            self.__food_calories[i].food = new_food
            self.__food_calories[i].calories = new_calories
        self.__has_unsaved_changes = True
    
    def find_records_on_day(self, day:int) -> list:
        records_list = []
        i = 0
        len_food_calories = len(self.__food_calories)
        while (i < len_food_calories):
            if (day == self.__food_calories[i].day):
                records_list.append(self.__food_calories[i])  
            i += 1       
        return records_list
            
    def calculate_total_calories(self, day: int) -> int:
        total_calories = 0
        i = 0
        len_food_calories = len(self.__food_calories)
        while (i < len_food_calories):
            if (day == self.__food_calories[i].day):
                total_calories += self.__food_calories[i].calories
            i += 1           
        return total_calories

    def calculate_steps(self, steps: int) -> float:
        if (steps != 0):
            calories_burned = steps * 0.04
        else:
            raise ZeroDivisionError("Cannot calculate.")
        return calories_burned

    def calculate_bmi(self, weight:int , height:float) -> float:
        if (weight > 0) and (height > 0):
            bmi = weight/(height*height)
        else:
            raise ZeroDivisionError("Cannot calculate.")
        return bmi    

    def bmi_status(self, bmi_value:float) -> str:
        bmi_text = ""
        if bmi_value <= 16:
            bmi_text += "You are very underweight."
        elif bmi_value <= 18.5:
            bmi_text += "You are underweight."
        elif bmi_value <= 25:
            bmi_text += "Congrats! You are healthy."
        elif bmi_value <= 30:
            bmi_text += "You are overweight."
        else:
            bmi_text += "You are very overweight."
        return bmi_text
