import pandas as pd
#df = pd.read_csv(r"/Users/shishirporeddy/Documents/GitHub/INST326-Final-Project-/College Park Apartment Database_Version1 - Sheet1.csv")
#print(df) 

#df q= pd.read_excel(r"/Users/shishirporeddy/Desktop/INST326/College Park Apartment Database_Version1.xlsx#")
#print(df)
#url="https://docs.google.com/spreadsheets/d/1F8AL1BA8NFl0uHObNFIyygi7sBF6MP3TBv1jbXa7OWg/edit?usp=sharing" 
#s=requests.get(url).content 
#c=pd.read_csv(s)
class Apartment:
    
    def __init__(self):
        #Members who worked on this method: Avi, Philip, Jhemel, and Shishir.
        
        # Read the CSV files
        self.apartments_df = pd.read_csv(r"CP Apartments_Version2.csv")
        self.amenities_df = pd.read_csv(r"Amenities.csv")
        self.merged_data = self.apartments_df.merge(self.amenities_df, 
                                                    on=["Apartment Name"])
        #return(self.merged_data)       
        # Store the apartment names and minimum budgets in a dictionary
        #self.min_budgets = dict(zip(self.merged_data["Apartment Name"], 
        # self.merged_data["Minimum Price"]))
        self.apartment_names = self.merged_data["Apartment Name"].unique()
       
       
        # Initialize user attributes to None
        self.user_name = None
        self.user_budget = None
        self.user_location = None
        self.user_pool = None
        self.user_gym = None
        self.user_parking = None
        self.user_electronic_entry_locks = None
        self.user_study_rooms = None
        self.user_game_lounge = None

    def userBudget(self,user_input_budget):
        #Members who worked on this method: Shishir

        user_input_budget = int(input("What is your minimum budget?")) 
        cheapest_apt=min(self.min_budget.values)
        matching_apartments = [key for key in self.min_budget if self.min_budget[key] <= user_input_budget]
        if not matching_apartments:
            raise ValueError("Your budget does not meet the minimum budget for any of the apartments")
        elif user_input_budget >= self.min_budget["Terrapin Row"]:
            return f'You meet the minimum budget of Terrapin Row: {self.min_budget["Terrapin Row"]}'
        elif user_input_budget >= self.min_budget["University View"]:
            return f'You meet the minimum budget of University View: {self.min_budget["University View"]}'
        elif user_input_budget >= self.min_budget["The Varsity"]:
            return f'You meet the minimum budget of The Varsity: {self.min_budget["The Varsity"]}'
        else:
            return f'Your budget satisfies the minimum budget of Terrapin Row \
        ({self.min_budget["Terrapin Row"]}), University View \
        ({self.min_budget["University View"]}), and The Varsity \
        ({self.min_budget["The Varsity"]})'




    def userInput(self):
        #Members who worked on this method: Avi and Philip
        
        print("Please answer the following questions for us to help provide you with your ideal apartment")
        user_name = input("Please enter your full name:")
        
        
        #userBudget()
        #user_location  and apt_some_location aren't used at the moment, but
        # will be used in the future
        
        user_location = input("Which part of UMD campus would be ideal for you."
                              " Type North or South: ") 
    
                 
        apt_some_location = ["Terrapin Row is South","University View is North",
                             "The Varsity is North"] 
        
        userInputCounter = 0

        user_pool=int(input("Are you looking for a pool? Type 0 for no pool or 1"  
                        " for pool:")) 
        userInputCounter += user_pool
        user_gym=int(input("Are you looking for a gym? Type 0 for no gym or 1" 
                        " for gym:"))
        userInputCounter += user_gym
        user_parking=int(input("Are you looking for parking? Type 0 for no" 
                            " parking and 1 for parking:" ))
        userInputCounter += user_parking
        user_electronic_entry_locks=int(input("Do you want an apartment with an"
                                        " electronic entry lock system? Type 0"
                                        " for no system and 1 for a system:"  )) 
        userInputCounter += user_electronic_entry_locks
        user_study_rooms=int(input("Are you looking for study rooms? Type 0 for"
                               " no study rooms and 1 for study rooms:"))
        userInputCounter += user_study_rooms
        user_game_lounge=int(input("Are you looking for game lounge? Type 0 for" 
                                   " no game lounge and 1 for a game lounge:"))
        userInputCounter += user_game_lounge


        terrapinRow_Amenity_Counter = 6
        universityView_or_theVarsity_Amenity_Counter = 3
        if userInputCounter>= terrapinRow_Amenity_Counter:
            print("Apartment with your ideal amenities: Terrapin Row")
        elif userInputCounter>= universityView_or_theVarsity_Amenity_Counter:
            print("Apartments with your ideal amenities: University View and" 
                  " The Varsity")
        else:
            print("None of these apartments have the amenities that you are" 
                  " looking for.")


        # Initialize variables
#best_apartment = None
#highest_score = 0

# Iterate through each apartment
#for apartment in apartments:
    # Calculate score for current apartment
    #score = (apartment['rent'] - (apartment['distance'] * 0.1)) / apartment['rooms']
    
    # Update best_apartment if current apartment has a higher score
    #if score > highest_score:
        #best_apartment = apartment['number']
        #highest_score = score
    #return best_apartment

    #Possible way to find apartment that fits user's amenitites needs:
    #if user_pool==1 and user_gym==1 and user_parking==1 and \
         #user_electronic_entry_locks==1 and user_study_rooms==1 and \
        #user_game_lounge ==1:
    #return "Terrapin Row"
    #Find a more efficent way to do this by traversing the merged csv file.




    def check_eligibility(self):
        """
        Check if user meets all the proper documentation for leasing.

        Args:
        - identity_proof: string, proof of identity (e.g. driver's license, passport)
        - income_proof: string, proof of income (e.g. pay stub, bank statement)
        - residency_proof: string, proof of current residency (e.g. utility bill, lease agreement)
        - insurance_proof: string, proof of insurance (e.g. auto insurance, renters insurance)

        Returns:
        - eligible: boolean, True if user meets all the proper documentation, False otherwise
        """
        #Members who worked on this method: Jhemel
        
        identity_proof = int(input("Do you have proof of identity (e.g. driver's license, passport) ? Type 0 for no, 1 for yes:")) 
        income_proof = int(input("Do you have proof of income (e.g. pay stub, bank statement) ? Type 0 for no, 1 for yes:")) 
        identity_proof = int(input("Do you have proof of current residency (e.g. utility bill, lease agreement) ? Type 0 for no, 1 for yes:")) 
        insurance_proof = int(input("Do you have proof of insurance (e.g. auto insurance, renters insurance) ? Type 0 for no, 1 for yes:"))                
 
        
        
        
        
        # Check if all proofs of documentation are provided
        if identity_proof == 1 and income_proof == 1 and residency_proof == 1 and insurance_proof == 1:
            return("You have all the required documentation to live in these apartments")
            
        else:
            return("Please provide all the required documentation.")
        
        
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
        



#We will implement this main method in the future.
#def main():
    #apt = Apartment()
    
    #apt.userInput()
    
#if __name__=='__main__':
    #main()

        



            
        
   
              
                
                







