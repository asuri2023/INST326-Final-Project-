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

    def check_eligibility(self, some_name, proof_of_identity, proof_of_income):
        """
        Check if user meets all the proper documentation for leasing.

        Args:
        - identity_proof: string, proof of identity (e.g. driver's license, 
            passport)
        - income_proof: string, proof of income (e.g. pay stub, 
            bank statement)
        - residency_proof: string, proof of current residency (e.g. utility 
            bill, lease agreement)
        - insurance_proof: string, proof of insurance (e.g. auto insurance, 
            renters insurance)

        Returns:
        - eligible: boolean, True if user meets all the proper documentation, 
            False otherwise
        """
        #Member who worked on this method: Jhemel
        #Technique used: Conditional Expression
        
        
        

        
        if proof_of_identity == "yes" and proof_of_income == "yes":
            print(f"{some_name}, you are eligible to lease an apartment in College Park.")
            self.proof_of_identity_boolean = True
            self.proof_of_income_boolean = True

        elif proof_of_identity == "yes" and proof_of_income == "no":
            print(f"{some_name}, you are not eligible to lease an apartment in College Park." 
            "\nPlease provide proof of income to proceed further.")
            self.proof_of_identity_boolean = True
            self.proof_of_income_boolean = False
        elif proof_of_identity == "no" and proof_of_income == "yes":
            print(f"{some_name}, you are not eligible to lease an apartment in College Park." 
            "\nPlease provide proof of identity to proceed further.")
            self.proof_of_identity_boolean = False
            self.proof_of_income_boolean = True
        else:
            return(f"{some_name}, you are not eligible to lease an apartment in College Park.")
        
        result = "Identity and income verified." if proof_of_identity == True and proof_of_income == True else "Identity and/or income not verified"
        print(result)

        # Will be used in the future:
            # Check if the user meets the minimum income requirement
            #min_income_requirement = 30000  # set a minimum income requirement of $30,000
            #if income_proof < min_income_requirement:
                
                #print("Your income does not meet the minimum requirement.")
                #return False
            
            # Check if the residency proof is current
            # You could implement this check by comparing the date on the residency_proof to today's date
            
            # Check if the insurance proof is valid
            # You could implement this check by verifying that the insurance policy is currently active
            
            # If all checks pass, the user is eligible
            #print("Congratulations, you are eligible to lease!")
            #return True    
                
        #Prof's advice: 
        #  Make the method more generic 
        #  return True if eligible or False if not eligible
            
        
        # Will be used in the future:
            # Check if the user meets the minimum income requirement
            #min_income_requirement = 30000  # set a minimum income requirement of $30,000
            #if income_proof < min_income_requirement:
                
                #print("Your income does not meet the minimum requirement.")
                #return False
            
            # Check if the residency proof is current
            # You could implement this check by comparing the date on the residency_proof to today's date
            
            # Check if the insurance proof is valid
            # You could implement this check by verifying that the insurance policy is currently active
            
            # If all checks pass, the user is eligible
            #print("Congratulations, you are eligible to lease!")
            #return True
    
    def find_shared_group_apartment(self, num_people, some_apartment, budget):
        """
        Finds apartments that can accommodate a group of people with the given criteria.

        Args:
        - num_people (int): The number of people who want to live together in the apartment.
        - some_apartment (str): The apartment chosen by the user.
        - budget (float): The monthly rent per person in the group for the chosen apartment.
        Returns:
        - A list of apartments that meet the given criteria.
        """
    # #Techniques used: f-strings containing expressions
    # #Member who worked on this method: Jhemel
    # Assume we have a list of available apartments with their details
        chosen_apartment_df =  self.apartments_df[ self.apartments_df['Apartment Name'] == self.chosen_apartment]
        #print(chosen_apartment_df)
        chosen_rooms_available_df = chosen_apartment_df[chosen_apartment_df['Number of Rooms Available']>= self.num_people ]
        print("\nThese are the rooms available that can fit the number of tenants:")
        print(chosen_rooms_available_df)

        chosen_apartment_number = int(input("\nWhich of the apartment units listed best fit your needs?"
        "\nPlease specify the Apartment Number of the unit shown under the Apartment Number column (e.g. 500):" ))
        apartment_number_df = chosen_apartment_df[chosen_apartment_df['Apartment Number']== chosen_apartment_number]
        
        #f-strings containing expressions
        print(f"\n{self.user_name}, this is the apartment unit's information:")
        print(apartment_number_df)
        
        #f-strings containing expressions
        print(f"This is the monthly rent that each of the tenants have to pay (including you): ${budget}.")