import re
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

class Apartment:
    
    def __init__(self):
        #Member who worked on this method: Avi
        #Technique used: Sequence unpacking
        
        # Read the CSV files
        self.apartments_df = pd.read_csv(r"CP Apartments_Version3.csv")
        self.amenities_df = pd.read_csv(r"Amenitites_Version2.csv")
        self.historical_df = pd.read_csv(r"Major Historical Data_Version3.csv")
        
        # Merging operation on Pandas DataFrames
        self.merged_data = self.apartments_df.merge(self.amenities_df, 
                                                    on=["Apartment Name"])
        
            
        # Will be used in the future:
            # Store the apartment names and minimum budgets in a dictionary
            #self.min_budgets = dict(zip(self.merged_data["Apartment Name"], 
            # self.merged_data["Minimum Price"]))
            
        self.terrapin_row, self.university_view, self.the_varsity, self.south_campus_commons = self.merged_data["Apartment Name"].unique()
        self.min_budget = {"Terrapin Row":1250, "University View":1200, 
                           "The Varsity":1104, "South Campus Commons":1016} 
        
        
        self.major_campus_dictionary=  {1: ["University View","The Varsity"],
                                   2:["Terrapin Row","South Campus Commons"],
                                   3: ["Terrapin Row","South Campus Commons"],
                                   4:["University View","The Varsity"],
                                   5:["Terrapin Row","South Campus Commons"]}
        
             
       
        # Initialize user attributes to None
        self.user_name = None
        self.proofOfIdentity = None
        self.proofOfIncome = None
        self.proof_of_identity_boolean = False
        self.proof_of_income_boolean = False
        self.user_budget = None
        self.user_location = None
        self.user_pool = None
        self.user_gym = None
        self.user_parking = None
        self.user_electronic_entry_locks = None
        self.user_study_rooms = None
        self.user_game_lounge = None
        self.user_input_budget=None  
        self.major_category_input=None
        self.apartment1=None
        self.apartment2=None
        
        # User's chosen apartment attributes
        self.chosen_apartment=None
        self.num_people=None
        self.chosen_apartment_budget=None
        
        # User's profile attributes
        self.full_name = None
        self.email = None
        self.phone = None

    def submitApplication(self, some_apartment, some_name, some_email, some_Phone):
        #Member who worked on this method: Avi
        #Technique used: regular expressions
        name=None
        email=None
        phone=None
        
        validated_dict = {name:some_name, email:some_email, phone:some_Phone}
        
        # validate user input with regular expressions
        name_regex = r'[A-Za-z]\S+ .+?[A-Za-z\d]+$'
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        phone_regex = r'^\d{3}-\d{3}-\d{4}$'
        
        if not re.match(name_regex, some_name):
            print("Invalid name. Please enter a valid name.")
            
        
        if not re.match(email_regex, some_email):
            print("Invalid email. Please enter a valid email address.")
            
        
        if not re.match(phone_regex, some_Phone):
            print("Invalid phone number. Please enter a valid phone number in the format xxx-xxx-xxxx.")
        
        for key in validated_dict:
            if (not re.match(name_regex, str(validated_dict[key]))) and \
            (not re.match(email_regex, str(validated_dict[key]))) and \
            (not re.match(phone_regex, str(validated_dict[key]))):
                return False
        return True

            # if key in validated_dict != name_regex & key in validated_dict != email_regex & key in validated_dict != phone_regex:
            #     return False   
            # else: 
            #     return True